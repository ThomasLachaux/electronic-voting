import random
import utils.math
from utils.constants import p, g

def encrypt(message, pubkey):
  r = random.randint(1, p)
  c2 = utils.math.exponentiation(g, r, p)
  
  k = utils.math.exponentiation(pubkey, r, p)
  c1 = message * k % p

  return c1, c2

def decrypt(c1, c2, election_privkey):
  # TODO: c'est quoi ce k ?
  k = utils.math.exponentiation(c2, election_privkey, p)
  p_1_x = p - 1 - election_privkey
  k_1 =  utils.math.exponentiation(c2, p_1_x, p)
  m = c1 * k_1 % p

  return m