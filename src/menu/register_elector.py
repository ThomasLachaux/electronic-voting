from hashlib import new
from PyInquirer import prompt
import json
from os import path


questions = [{
    'type': 'input',
    'name': 'firstname',
    'message': 'Prénom ?'
  }, {
    'type': 'input',
    'name': 'lastname',
    'message': 'Nom de famille ?'
  }, {
    'type': 'input',
    'name': 'email',
    'message': 'Email ?'  
  }]

def entrypoint():
    new_user = prompt(questions)


    basepath = path.dirname(__file__)
    file = open(path.join(basepath, f'../database/users.json'), 'r+')
    users = json.load(file)
    print(users)
    
    users.append(new_user)
    file.seek(0)
    file.write(json.dumps(users))
    file.truncate()
    
    file.close()

