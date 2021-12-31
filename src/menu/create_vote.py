import glob
from os import path
from PyInquirer import prompt

def entrypoint(a, e, s):
  elections = [e['name'] for e in a.elections.values()]

  questions = {
    'type': 'list',
    'name': 'election',
    'message': 'Choisissez une election',
    'choices': elections
  }

  answer = prompt(questions)
  answer['election']


if __name__ == '__main__':
  entrypoint()