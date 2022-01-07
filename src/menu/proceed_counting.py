from PyInquirer.prompt import prompt
from rich import box
from rich.align import Align
import utils.password
import utils.elgamal
from utils.terminal import print_title
from rich.console import Console
from rich.table import Table
import shutil


def entrypoint(a, e, s):
  print_title('Compter les votes')


  elections = [{'name': election['name'], 'value': election_id} for election_id, election in s.elections.items()]

  question = [{
    'type': 'list',
    'name': 'election',
    'message': 'Quelle election voulez-vous dépouiller ?',
    'choices': elections
  }]

  answer = prompt(question)

  election_id = answer['election']
  election = s.elections[election_id]
  trusteds = a.elections[election_id]['trusteds']


  common_privkey = 0
  for trusted in trusteds:
    question = {
      'type': 'password',
      'name': 'password',
      'message': f"Entrez le mot de passe de {trusted['name']}"
    }

    password = prompt(question)['password']
    private_key = utils.password.generate_pkdf2(password, election_id)

    common_privkey += private_key


  # Init results to 0
  results = [0 for a in election['candidates']]

  for vote in election['results']:
    decrypted_vote = utils.elgamal.decrypt(vote[0], vote[1], common_privkey)
    
    # Remove one for security
    decrypted_vote -= 1

    results[decrypted_vote] += 1

  console = Console()
  print_title('🏆 Résultat des élections 🏆')

  term_columns, term_rows = shutil.get_terminal_size()
  table = Table(expand=True, box=box.SQUARE, width=int(term_columns * 3 / 4))

  table.add_column('Candidats', style='green', width=int(term_columns * 3 / 8))
  table.add_column('Voix', justify='right', style='red', width=int(term_columns * 3 / 8))
  for result_id, result in enumerate(results):
    table.add_row(election['candidates'][result_id], str(result))

  table = Align.center(table)
  console.print(table)
  input()
  