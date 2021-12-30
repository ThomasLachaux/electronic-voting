import glob
from os import path
from PyInquirer import prompt

def list_elections():
  basepath = path.dirname(__file__)

  json_files = [f for f in glob.glob(f'{basepath}/../database/elections/*.json')]

  elections = [e.split('/')[-1][:-5] for e in json_files]
  
  return elections

def entrypoint():

  questions = {
    'type': 'list',
    'name': 'election',
    'message': 'Choisissez une election',
    'choices': list_elections()
  }

  answer = prompt(questions)
  answer['election']


if __name__ == '__main__':
  entrypoint()