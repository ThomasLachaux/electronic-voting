import random
import hmac
import hashlib

base = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def generate_password():
  password = ""
  for i in range(15):
    password += random.choice(base)

  return password


def generate_pkdf2(c, election_uuid):
  hash = hashlib.pbkdf2_hmac('sha256', c.encode(), election_uuid.encode(), 1000)

  return int.from_bytes(hash, 'big')
