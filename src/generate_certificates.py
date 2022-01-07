import utils.elgamal
import utils.math
import utils.password
from utils.constants import g, p
import json
from os import path

working_dir = path.dirname(__file__)

file = open(path.join(working_dir, 'database/ca.json'), 'r')
ca_keys = json.load(file)
file.close()

password = utils.password.generate_password()
private = utils.password.generate_pkdf2(password, "Election")

pubkey =  utils.math.exponentiation(g, private, p)
print(f'Public key {pubkey}')
print(f'Private key {private}')

certificate = utils.elgamal.sign(ca_keys['privkey'], pubkey)
print(f'Certificate {certificate}')
