from PyInquirer import prompt
import json
from os import path
from servers import serverA, serverE


def ask_multiple_items(item_name: str):
  items = []

  while True:
    if len(items) > 0:
      print(f'{item_name.capitalize()} : {" ".join(items)}')

    items_questions = [{
    'type': 'input',
    'name': 'name',
    'message': f"Nom {len(items) + 1} (vide pour terminer)"
    }]

    item = prompt(items_questions)

    # If answered empty
    if not item['name']:
      if len(items) == 0:
        print(f'Veuillez ajouter au moins un {item_name}')

      else:
        break
    # Otherwise, add the candidate
    else:
      items.append(item['name'])

  return items

main_questions = [{
    'type': 'input',
    'name': 'election_name',
    'message': 'Titre de l\'election'
  }]

def entrypoint():
  election_name = prompt(main_questions)

  candidates = ask_multiple_items('candidats')
  trusteds = ask_multiple_items('dépouilleur')

  print(candidates)
  print(trusteds)

  a = serverA.serverA()
  e = serverE.serverE()
  a.create_election(election_name['election_name'], candidates, e)
  e.send_pubkeys(a)