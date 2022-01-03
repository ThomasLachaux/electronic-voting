import hashlib
import random
import utils.math
import utils.password
from utils.constants import g, p

def prove(election_id, secret):

  w = random.randint(1, p)
  a = utils.math.exponentiation(g, w, p) 

  # Dérivation de clé
  s = utils.password.generate_pkdf2(secret, election_id)

  # Génération de clé publique
  pubkey = utils.math.exponentiation(g, s, p)

  # Génération du challenge
  challenge_proof = hashlib.sha256(str(pubkey + a).encode())
  challenge = int.from_bytes(challenge_proof.digest(), 'big')

  challenge_response = (w - s * challenge) % p 
  return challenge_response, challenge

def verify(challenge_response, s, challenge_proof):
  a = (utils.math.exponentiation(g, challenge_response, p) * utils.math.exponentiation(s, challenge_proof, p)) % p
  challenge_verify = hashlib.sha256(str(s + a).encode())
  challenge = int.from_bytes(challenge_verify.digest(), 'big')

  return challenge == challenge_proof