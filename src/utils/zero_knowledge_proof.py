import hashlib
import random
import utils.math
import utils.password

def prove(g, p, election_id):

  w = random.randint(1, p)
  a = utils.math.exponentiation(g, w, p)

  # TODO Passer su PyInquierer
  secret = input("enter your password: ")
  s = utils.password.generate_pkdf2(secret, election_id)
  print(s)
  chal_proof = hashlib.sha256(str(s + a).encode())
  val = int.from_bytes(chal_proof.digest(), 'big')
  resp = (w - val * int(secret, 36)) % p

  return resp, val

def verify(g, p, resp, s, chal):
  a = (utils.math.exponentiation(g, resp, p) * utils.math.exponentiation(s, chal, p)) % p
  print(s)
  chal_verify = hashlib.sha256(str(s + a).encode())
  val = int.from_bytes(chal_verify.digest(), 'big')
  if val == chal:
    print("success")
  else:
    print("c'est pas bon")