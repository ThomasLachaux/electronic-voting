import uuid
import random
import utils.password, utils.math, utils.prime


pubC_list = []


for user in e_users:
  # TODO create stronger passwords
  password = utils.password.generate_password()
  s = utils.password.generate_pkdf2(password, election_uuid)
  pubkey =  utils.math.exponentiation(credentials_g, s, credentials_p)
  pubC_list.append(pubkey)
  user['c'] = password
  user['pubC'] = pubkey  

random.shuffle(pubC_list)
