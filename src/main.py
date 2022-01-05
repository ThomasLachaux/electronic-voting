from PyInquirer import prompt
import utils.elgamal
import utils.zero_knowledge_proof
import random
from servers import serverA
from servers import serverE
from servers import serverS



questions = {
  'type': 'list',
  'name': 'menu',
  'message': 'Bonjour ô maître Rémi ! Comme puis-je aider votre Sainteté ?',
  'choices': [
    {'name': 'Créer une élection', 'value': 'create_election'},
    {'name': 'Créer un electeur', 'value': 'create_elector'},
    {'name': 'Créer un vote', 'value': 'create_vote'},
    {'name': 'Vérifier un vote', 'value': 'check_vote'},
    {'name': 'Procéder au dépouillement', 'value': 'proceed_counting'},
    {'name': 'Supprimer des données', 'value': 'delete_data'},
    {'name': 'Quitter', 'value': 'quit'}
  ]
}

a = serverA.serverA()
e = serverE.serverE()
s = serverS.serverS()

a.set_servers(e, s)
e.set_servers(a, s)
s.set_servers(a, e)

while True:
  answer = prompt(questions)['menu']

  if answer == 'quit':
    break

  submenu = __import__(f"menu.{answer}", fromlist=[None])
  submenu.entrypoint(a, e, s) 

print('Au revoir')