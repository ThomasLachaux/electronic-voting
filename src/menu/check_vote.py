from PyInquirer.prompt import prompt
from rich import box
from rich.align import Align

from utils.terminal import print_title
from rich.console import Console
from rich.table import Table
import shutil


def entrypoint(a, e, s):
  print_title('Vérifier un vote')
  console = Console()

  term_columns, term_rows = shutil.get_terminal_size()
  table = Table(expand=True, box=box.SQUARE, width=int(term_columns * 3 / 4))

  table.add_column('Signatures', style='green', justify='center')

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

  console.clear()
  print_title('Vérifier un vote')
  
  for index, signature in enumerate(s.elections[election_id]['signatures']):
    table.add_row(signature)

  table = Align.center(table)
  console.print(table)
  input()
  