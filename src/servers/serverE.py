import uuid
import json
from os import path
import utils.password, utils.math
import random
import copy

# TODO: bouger ca
credentials_p = 32317006071311007300338913926423828248817941241140239112842009751400741706634354222619689417363569347117901737909704191754605873209195028853758986185622153212175412514901774520270235796078236248884246189477587641105928646099411723245426622522193230540919037680524235519125679715870117001058055877651038861847280257976054903569732561526167081339361799541336476559160368317896729073178384589680639671900977202194168647225871031411336429319536193471636533209717077448227988588565369208645296636077250268955505928362751121174096972998068410554359584866583291642136218231078990999448652468262416972035911852507045361090559
credentials_g = 2


class serverE():
  """
    Le serveur E connait la liste des utilisateurs (leur info perso), ainsi que leur clé publique
  """
  def __init__(self):
      basepath = path.dirname(__file__)
      self.db_path = path.join(basepath, f'../database/server_e.json')
      
      self.load()

  def set_servers(self, a, s):
    self.server_a = a
    self.server_s = s


  def create_election(self, election_id, election):

    # Transform user array into user object
    new_users = {}

    for user in election['users']:

      user_id = str(uuid.uuid4())

      new_users[user_id] = user

      password = utils.password.generate_password()
      new_users[user_id]['c'] = password

      s = utils.password.generate_pkdf2(password, election_id)
      pubkey =  utils.math.exponentiation(credentials_g, s, credentials_p)
      new_users[user_id]['pubkey'] = pubkey  

    election['users'] = new_users

    self.elections[election_id] = election
    self.save()

    # Create pubkeys list
    pubkeys = [user['pubkey'] for user in election['users'].values()]
    random.shuffle(pubkeys)

    # Send pubkeys to S
    self.server_a.elections[election_id]['pubkeys'] = pubkeys
    self.server_a.save()

    # Send pubkeys to S and election data
    self.server_s.elections[election_id] = {'pubkeys': pubkeys, 'name': election['name'], 'candidates': election['candidates']}
    self.server_s.save()


  def save(self):
    file = open(self.db_path, 'w')
    file.write(json.dumps({'elections': self.elections}, indent=4))
    file.close()

  def load(self):
    if path.isfile(self.db_path):
      file = open(self.db_path, 'r')
      data = json.load(file)
      self.elections = data['elections']

    else:
      self.elections = {}
