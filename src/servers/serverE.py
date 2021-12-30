import uuid
import json
from os import path
import utils.password, utils.math
import random

# TODO: bouger ca
credentials_p = 32317006071311007300338913926423828248817941241140239112842009751400741706634354222619689417363569347117901737909704191754605873209195028853758986185622153212175412514901774520270235796078236248884246189477587641105928646099411723245426622522193230540919037680524235519125679715870117001058055877651038861847280257976054903569732561526167081339361799541336476559160368317896729073178384589680639671900977202194168647225871031411336429319536193471636533209717077448227988588565369208645296636077250268955505928362751121174096972998068410554359584866583291642136218231078990999448652468262416972035911852507045361090559
credentials_g = 2

class serverE():
  
  def create_election(self, election_id, election_name, candidates, users):
    for user in users:
      user['uuid'] = str(uuid.uuid4())
      
      password = utils.password.generate_password()
      user['c'] = password

      s = utils.password.generate_pkdf2(password, election_id)
      pubkey =  utils.math.exponentiation(credentials_g, s, credentials_p)
      user['pubkey'] = pubkey  


    basepath = path.dirname(__file__)
    file = open(path.join(basepath, f'../database/elections/{election_name}.json'), 'w')
    file.write(json.dumps({'id': election_id, 'name': election_name, 'candidates': candidates, 'users': users}, indent=4))
    file.close()

  # permet d'acceder à la pubkey des trusted
    file = open(path.join(basepath, f'../database/trusted.json'), 'r')
    config = json.load(file)
    trusted_pubkey = config[0]["trusted_pubkey"]
    file.close()
    self.trusted_pubkey = trusted_pubkey
    self.users = users

  def send_pubkeys(self, serverA):
    pubkeys = [user['pubkey'] for user in self.users]
    random.shuffle(pubkeys)
    trusted_pubkey = self.trusted_pubkey

    serverA.pubkeys = pubkeys
    serverA.trusted_pubkey = trusted_pubkey