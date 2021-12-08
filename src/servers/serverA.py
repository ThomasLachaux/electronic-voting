from os import path
import json
import uuid

class serverA():

  def __init__(self):
    self.pubkeys = []

    # Load users.json
    basepath = path.dirname(__file__)
    file = open(path.join(basepath, '../database/users.json'), 'r')
    self.users = json.load(file)
    file.close()

  # au démarrage, load user.json
  def create_election(self, election_name, serverE):
    election_id = str(uuid.uuid4())

    serverE.create_election(election_id, election_name, self.users)