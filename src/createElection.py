import uuid
import random
import utils.password

election_uuid = '6e5a5e7a-bf28-4fd7-882f-bc32180f9806'

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

  prime = 8790983876703039375276380170349151573129340767447446224601093198268145005019968562588520506029452356771863978219815720626738141073037919012019521143795973

  


  


print(e_users)