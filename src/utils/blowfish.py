from Crypto.Cipher import Blowfish
from struct import pack
import random

block_size = Blowfish.block_size

def generate_secret_key():
  return random.randint(10 ** 48, 10 ** 49 - 1)

def encrypt(key, message):
  cipher = Blowfish.new(str(key).encode(), Blowfish.MODE_CBC)
  plen = block_size - len(message.encode()) % block_size
  padding = [plen]*plen
  padding = pack('b'*plen, *padding)

  return cipher.iv + cipher.encrypt(message.encode() + padding)

def decrypt(key, encrypted):
  iv = encrypted[:block_size]
  text = encrypted[block_size:]

  cipher = Blowfish.new(str(key).encode(), Blowfish.MODE_CBC, iv)

  decrypted = cipher.decrypt(text)
  last_byte = decrypted[-1]

  decrypted = decrypted[:-last_byte]

  return decrypted.decode()


