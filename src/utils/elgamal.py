import random
import utils.math

def encrypt(message, pubkey, p , g):
  r = random.randint(1, p)
  c2 = utils.math.exponentiation(g, r, p)
  
  k = utils.math.exponentiation(pubkey, r, p)
  c1 = message * k

  return c1, c2

def decrypt(c1, c2, p, election_privkey):
  k = utils.math.exponentiation(c2, election_privkey, p)
  k_1 =  utils.math.invert(k,p)
  m = c1 * k_1

  return m