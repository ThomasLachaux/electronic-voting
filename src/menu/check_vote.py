from PyInquirer.prompt import prompt


def entrypoint(a, e, s):
  questions = [
    {
      'type': 'input',
      'name': 'election_id',
      'message': 'Entrez l\'identifiant de l\'election'
    },
    {
      'type': 'input',
      'name': 'signature',
      'message': 'Entrez votre signature de vote',
    }
  ]

  answers = prompt(questions)
  
  signatures = s.elections[answers['election_id']]['signatures']

  if answers['signature'] in signatures:
    print('Votre vote est bien compté !')

  else:
    print('Votre vote n\' a pas été compté')