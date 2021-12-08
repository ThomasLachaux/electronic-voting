import uuid
import random
import utils.password, utils.math, utils.prime

election_uuid = str(uuid.uuid4())
credentials_p = 32317006071311007300338913926423828248817941241140239112842009751400741706634354222619689417363569347117901737909704191754605873209195028853758986185622153212175412514901774520270235796078236248884246189477587641105928646099411723245426622522193230540919037680524235519125679715870117001058055877651038861847280257976054903569732561526167081339361799541336476559160368317896729073178384589680639671900977202194168647225871031411336429319536193471636533209717077448227988588565369208645296636077250268955505928362751121174096972998068410554359584866583291642136218231078990999448652468262416972035911852507045361090559
credentials_g = 2
pubC_list = []
a_users = [
  {'firstname': 'Yohann', 'lastname': 'Valo', 'email': 'yvalo@gmail.com'},
  {'firstname': 'Thomas', 'lastname': 'de Lachaux', 'email': 'tdelachaux@gmail.com'}
]

for user in a_users:
  user['uuid'] = str(uuid.uuid4())


# Transmet la liste à E
e_users = a_users


for user in e_users:
  # TODO create stronger passwords
  password = utils.password.generate_password()
  s = utils.password.generate_pkdf2(password, election_uuid)
  pubkey =  utils.math.exponentiation(credentials_g, s, credentials_p)
  pubC_list.append(pubkey)
  user['c'] = password
  user['pubC'] = pubkey  

print(e_users)


random.shuffle(pubC_list)
print(pubC_list)