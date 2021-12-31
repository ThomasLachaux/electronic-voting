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

def entrypoint(a, e, s):
    new_user = prompt(questions)
    a.create_user(new_user)
    print('User created')


    

