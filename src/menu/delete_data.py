from PyInquirer import prompt
from utils.terminal import print_title

questions = [
  {
    'type': 'list',
    'name': 'scope',
    'message': 'Quelle élection supprimer ?',
    'choices': [
      {'name': 'Supprimer tous les utilisateurs', 'value': 'delete_users'},
      {'name': 'Supprimer toutes les elections', 'value': 'delete_elections'},
      {'name': 'Supprimer toutes les données', 'value': 'delete_all'}
    ]
  },
  {
    'type': 'confirm',
    'name': 'confirm',
    'message': 'En êtes-vous sûr ?',
    'default': False
  }
]


def delete_users(a, e, s):
  print('Suppression de tous les utilisateurs')

  a.users = []
  a.save()

def delete_elections(a, e, s):
  print('Suppression de toutes les elections')

  a.elections = {}
  a.save()

  e.elections = {}
  e.save()

  s.elections = {}
  s.save()

def entrypoint(a, e, s):  
  print_title('Supprimer des données')


  answer = prompt(questions)

  if not answer['confirm']:
    return

  if answer['scope'] == 'delete_users' or answer['scope'] == 'delete_all':
    delete_users(a, e, s)

  if answer['scope'] == 'delete_elections' or answer['scope'] == 'delete_all':
    delete_elections(a, e, s)


