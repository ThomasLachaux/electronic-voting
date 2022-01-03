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
  # Add + 1 for security
  candidate_id = answers['candidate_id'] + 1
  user_id = answers['user_id']
  user = election['users'][user_id]

  encrypted_candidate = utils.elgamal.encrypt(candidate_id, user['pubkey'])

  signature = utils.zero_knowledge_proof.prove(election_id, answers['secret'])

  ballot = {'election_id': election_id, 'user_id': user_id, 'encrypted_candidate': encrypted_candidate, 'signature': signature, 'pubkey': user['pubkey']}

  s.vote(ballot)

if __name__ == '__main__':
  entrypoint()