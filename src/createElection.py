import uuid
import random
import utils.password, utils.math

election_uuid = '6e5a5e7a-bf28-4fd7-882f-bc32180f9806'

generator = random.randint(1, prime - 1)


a_users = [
  {'firstname': 'Yohann', 'lastname': 'Valo', 'email': 'yvalo@gmail.com'},
  {'firstname': 'Thomas', 'lastname': 'de Lachaux', 'email': 'tdelachaux@gmail.com'}
]

for user in a_users:
  user['uuid'] = uuid.uuid4()


# Transmet la liste à E
e_users = a_users


for user in e_users:
  # TODO create stronger passwords
  user['c'] = random.randint(1000, 9999)
  password = utils.password.generate_password()
  s = utils.password.generate_pkdf2(password, election_uuid)

  prime = 14781221331231416261
  pubkey =  utils.math.exponentiation(generator, s, prime)

  print(pubkey)



  


print(e_users)