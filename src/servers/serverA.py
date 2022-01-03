from os import path
import json
import uuid
from copy import deepcopy

# TODO: Virer ça
example_trusted = {
    "name": "Trusted",
    "c": "TjNHnGhGu2FiYxc",
    "pubkey": 20200553798616432118079053271644308434917933566442211007971977506576269806574024562643800354143013478798433010976054756336076920309419888404142688331020306688089046192326802980468531561449860383021515533297425180730107597733770870871690485480436024269804226946996433552487134883551359198522049507480173539346466428264088448824277834334381228167168745103605868438301118559832494864899444882387161543617193597891446383876764046196260680006164806443868185121485214237388430773219872407967540388555352645662062147547962407595471139817938860327084800298403142384179264348439320279767172614588275807834154255544842891283265
}

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
  def create_election(self, election_name, candidates):
    election_id = str(uuid.uuid4())
    election = {'name': election_name, 'candidates': candidates, 'users': self.users}
    self.elections[election_id] = election

    # deep copy the election to pass the object by value and not reference
    self.server_e.create_election(election_id, deepcopy(election))

    election['trusteds'] = [example_trusted]
    self.save()



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

    else:
      self.elections = {}
      self.users = []
