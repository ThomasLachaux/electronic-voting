import uuid
import json
from os import path
import utils.password, utils.math
import random
import copy
from utils.constants import p, g
import utils.emails


class serverE():
  """
    Le serveur E connait la liste des utilisateurs (leur info perso), ainsi que leur clé publique
  """
  def __init__(self):
      basepath = path.dirname(__file__)
      self.db_path = path.join(basepath, f'../database/server_e.json')
      
      self.load()

  def set_servers(self, a, s):
    self.server_a = a
    self.server_s = s


  def create_election(self, election_id, election):

    # Transform user array into user object
    new_users = {}

    for user in election['users']:

      user_id = str(uuid.uuid4())

      new_users[user_id] = user

      password = utils.password.generate_password()
      new_users[user_id]['c'] = password

      s = utils.password.generate_pkdf2(password, election_id)
      pubkey =  utils.math.exponentiation(g, s, p)
      new_users[user_id]['pubkey'] = pubkey  

    election['users'] = new_users

    self.elections[election_id] = election
    self.save()

    # Create pubkeys list
    pubkeys = [user['pubkey'] for user in election['users'].values()]
    random.shuffle(pubkeys)

    # Send pubkeys to S
    self.server_a.elections[election_id]['pubkeys'] = pubkeys
    self.server_a.save()

    # Send pubkeys to S and election data
    self.server_s.elections[election_id] = {'pubkeys': pubkeys, 'name': election['name'], 'candidates': election['candidates'], 'voted': [], 'results': [], 'signatures': []}
    self.server_s.save()

    utils.emails.send_voter_email(election)


  def save(self):
    file = open(self.db_path, 'w')
    file.write(json.dumps({'elections': self.elections, 'private_key': self.private_key, 'public_key': self.public_key, 'certificate': self.certificate}, indent=4))
    file.close()

  def load(self):
    if path.isfile(self.db_path):
      file = open(self.db_path, 'r')
      data = json.load(file)
      self.elections = data['elections']
      self.private_key = data['private_key']
      self.public_key = data['public_key']
      self.certificate = data['certificate']

    else:
      self.elections = {}
