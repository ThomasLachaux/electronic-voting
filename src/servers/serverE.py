import uuid
import json
from os import path

class serverE():
  def create_election(self, election_id, election_name, users):
    for user in users:
      user['uuid'] = str(uuid.uuid4())
      user['pubc'] = str(uuid.uuid4())


    basepath = path.dirname(__file__)
    file = open(path.join(basepath, f'../database/elections/{election_id}.json'), 'w')
    file.write(json.dumps({'id': election_id, 'name': election_name, 'users': users}))
    file.close()

    self.users = users
