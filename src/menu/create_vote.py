import glob
from os import path
from PyInquirer import prompt
from utils.helpers import contains
import utils.elgamal
import utils.zero_knowledge_proof


def entrypoint(a, e, s):
  questions = [
    {
      'type': 'input',
      'name': 'user_id',
      'message': 'Entrez votre identifiant de vote'
    },
    {
      'type': 'list',
      'name': 'election',
      'message': 'Choississez une election',
      'choices': lambda answers: [{'name': election['name'], 'value': (election_id, election)} for election_id, election in e.elections.items() if answers['user_id'] in election['users']]
    },
    {
      'type': 'list',
      'name': 'candidate_id',
      'message': 'Choisissez un candidat',
      'choices': lambda answers: [{'name': candidate, 'value': candidate_id} for candidate_id, candidate in enumerate(answers['election'][1]['candidates'])]
    },
    {
      'type': 'password',
      'name': 'secret',
      'message': 'Entrez votre clé secrète'
    }
  ]

  answers = prompt(questions)
  
  election_id, election = answers['election']
  candidate_id = answers['candidate_id']
  user_id = answers['user_id']
  user = election['users'][user_id]

  encrypted_candidate = utils.elgamal.encrypt(candidate_id, user['pubkey'])

  zkp = utils.zero_knowledge_proof.prove(election_id, answers['secret'])

  ballot = {'election_id': election_id, 'user_id': user_id, 'encrypted_candidate': encrypted_candidate, 'zkp': zkp}

  s.vote(ballot)

  # demander a l'user son mail
  # Demander l'email à E (ou uuid car plus simple) => retrouver la clé publique 
  # demander sur quelle election il veut voter
  # demander le candidat
  # demander le mot passe
  # créer le ballot avec elgamal avec, l'id de l'election, l'uuid du votant, le vote chiffré, et la signateur ZKP
  # le serveur vérifie le ZKP, regarde si l'uuid du votant n'existe pas pour l'election, et l'ajoute

if __name__ == '__main__':
  entrypoint()