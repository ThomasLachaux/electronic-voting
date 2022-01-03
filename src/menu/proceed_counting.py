from PyInquirer.prompt import prompt
import utils.password
import utils.elgamal


def entrypoint(a, e, s):

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


  print("Resultat des élections: ")
  for result_id, result in enumerate(results):
    print(f"{election['candidates'][result_id]}: {result}")
  