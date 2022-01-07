import random
import utils.math
from utils.constants import p, g
import hashlib
import utils.prime
import utils.math
import math

def encrypt(message, pubkey):
  r = random.randint(1, p)
  c2 = utils.math.exponentiation(g, r, p)
  
  k = utils.math.exponentiation(pubkey, r, p)
  c1 = message * k % p

  return c1, c2

def decrypt(c1, c2, election_privkey):
  p_1_x = p - 1 - election_privkey
  k_1 =  utils.math.exponentiation(c2, p_1_x, p)
  m = c1 * k_1 % p

  return m

def sign(privkey_signer, message):
  s = 0
  while s == 0:

    # Generate a prime number relative to p - 1
    while True:
      k = random.randint(2, p - 2)

      if math.gcd(k, p - 1) == 1:
        break
  
    r = utils.math.exponentiation(g, k, p)
    k_1 = pow(k, -1, p - 1)

    h_object = hashlib.sha256(str(message).encode())
    h = int.from_bytes(h_object.digest(), 'big')
    s = ((h - privkey_signer * r ) * k_1) % (p - 1)

  return r, s

def verify_signature(message, publik_key, r, s):
  
  h_object = hashlib.sha256(str(message).encode())
  h = int.from_bytes(h_object.digest(), 'big')
  signature = (utils.math.exponentiation(publik_key, r, p) * utils.math.exponentiation(r, s, p)) % p

  return signature == utils.math.exponentiation(g, h, p)    

