from os import path
import json
import uuid
from copy import deepcopy
import utils.password
from utils.constants import g, p

class serverA():
  """
  Le serveur A connait la liste des utilisateurs (leurs info perso), ainsi qu'une liste de clé publiques mélangées par election
  """

  def __init__(self):
      basepath = path.dirname(__file__)
      self.db_path = path.join(basepath, f'../database/server_a.json')
      
      self.load()

  def set_servers(self, e, s):
    self.server_e = e
    self.server_s = s

  # au démarrage, load user.json
  def create_election(self, election_name, candidates, trusteds):
    election_id = str(uuid.uuid4())
    election = {'name': election_name, 'candidates': candidates, 'users': self.users}
    self.elections[election_id] = election

    # deep copy the election to pass the object by value and not reference
    self.server_e.create_election(election_id, deepcopy(election))

    common_privkey = 0

    trusteds_list = []
    for trusted_name in trusteds:
      password = utils.password.generate_password()
      s = utils.password.generate_pkdf2(password, election_id)
      pubkey = utils.math.exponentiation(g, s, p)

      trusted = {'name': trusted_name, 'c': password, 'pubkey': pubkey}
      trusteds_list.append(trusted)

      # Forge the common election public key
      common_privkey += s

    election['trusteds'] = trusteds_list
    self.save()

    # Generate the public key of the election
    common_pubkey = utils.math.exponentiation(g, common_privkey, p)

    # Add the common election public key to S and E
    self.server_s.elections[election_id]['election_privkey'] = common_privkey
    self.server_s.elections[election_id]['election_pubkey'] = common_pubkey
    self.server_s.save()

    self.server_e.elections[election_id]['election_privkey'] = common_privkey
    self.server_e.elections[election_id]['election_pubkey'] = common_pubkey
    self.server_e.save()


  def create_user(self, new_user):
    self.users.append(new_user)
    self.save()
  
  def save(self):
    file = open(self.db_path, 'w')
    file.write(json.dumps({'elections': self.elections, 'users': self.users}, indent=4))
    file.close()

  def load(self):
    if path.isfile(self.db_path):
      file = open(self.db_path, 'r')
      data = json.load(file)
      self.elections = data['elections']
      self.users = data['users']
      self.private_key = data['private_key']
      self.public_key = data['public_key']
      self.certificate = data['certificate']

    else:
      self.elections = {}
      self.users = []
