from os import path
import json
import utils.zero_knowledge_proof
import utils.elgamal
import utils.blowfish

class serverS():
  """
    Le serveur S connait la liste des clé publique des votants pour une election, et le vote pour chaque clé publique
  """
  
  def __init__(self):
      basepath = path.dirname(__file__)
      self.db_path = path.join(basepath, f'../database/server_s.json')
      
      self.load()

  def vote(self, encrypted_ballot, encrypted_key):
    secret_key = utils.elgamal.decrypt(encrypted_key[0], encrypted_key[1], self.private_key)
    serialized_ballot = utils.blowfish.decrypt(secret_key, encrypted_ballot)
    ballot = json.loads(serialized_ballot)

    challenge_response, challenge_proof, challenge_hash = ballot['signature']

    if not utils.zero_knowledge_proof.verify(ballot['pubkey'], challenge_response, challenge_proof):
      print('Code secret incorrect !')
      return False

    election = self.elections[ballot['election_id']]

    # If the user has already voted
    if ballot['pubkey'] in election['voted']:
      print("Dommage ! On ne vote qu'une fois !")
      return False

    election['voted'].append(ballot['pubkey'])
    election['results'].append(ballot['encrypted_candidate'])
    election['signatures'].append(challenge_hash)
    self.save()
    print('A voté !')

    print(f'Votre signature de vote est : {challenge_hash}')

    return challenge_hash

  def set_servers(self, a, e):
    self.server_a = a
    self.server_e = e

  def save(self):
    file = open(self.db_path, 'w')
    file.write(json.dumps({'elections': self.elections, 'private_key': self.private_key, 'public_key': self.public_key, 'certificate': self.certificate}, indent=4))
    file.close()

  def load(self):
    if path.isfile(self.db_path):
      file = open(self.db_path, 'r')
      data = json.load(file)
      self.elections = data['elections']
      self.private_key = data['private_key']
      self.public_key = data['public_key']
      self.certificate = data['certificate']

    else:
      self.elections = {}
