from PyInquirer import prompt
import json
from os import path
from servers import serverA, serverE

main_questions = [{
    'type': 'input',
    'name': 'election_name',
    'message': 'Titre de l\'election'
  }]



def entrypoint():
  election_name = prompt(main_questions)


  candidates = []

  while True:
    if len(candidates) > 0:
      print(f'Candidats : {" ".join(candidates)}')

    candidate_questions = [{
    'type': 'input',
    'name': 'name',
    'message': f"Nom du candidat {len(candidates) + 1} (vide pour terminer)"
    }]

    candidate = prompt(candidate_questions)

    # If answered empty
    if not candidate['name']:
      if len(candidates) == 0:
        print('Veuillez ajouter au moins un candidat')

      else:
        break
    # Otherwise, add the candidate
    else:
      candidates.append(candidate['name'])

    a = serverA.serverA()
    e = serverE.serverE()
    a.create_election(election_name['election_name'], candidates, e)
    e.send_pubkeys(a)