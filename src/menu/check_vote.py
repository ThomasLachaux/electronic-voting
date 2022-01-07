from PyInquirer.prompt import prompt


def entrypoint(a, e, s):

  questions = [
    {
      'type': 'list',
      'name': 'election',
      'message': 'Choisissez une election à vérifier',
      'choices': [{'name': election['name'], 'value': election_id } for election_id, election in s.elections.items()]
    }
  ]

  answer = prompt(questions)
  election_id = answer['election']
  
  print('Voici la liste des signatures pour cette election')
  for index, signature in enumerate(s.elections[election_id]['signatures']):
    print(f'{index + 1} - {signature}')

  