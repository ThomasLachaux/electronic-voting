from PyInquirer import prompt
import json
from os import path
from servers import serverA, serverE

questions = [{
    'type': 'input',
    'name': 'election_name',
    'message': 'Titre de l\'election'
  }]

def entrypoint():
  election_Name = prompt(questions)
  a = serverA.serverA()
  e = serverE.serverE()
  a.create_election(election_Name, e)
  e.send_pubkeys(a)