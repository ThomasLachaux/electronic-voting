from os import path
import json

class serverS():
  """
    Le serveur S connait la liste des clé publique des votants pour une election, et le vote pour chaque clé publique
  """
  
  def __init__(self):
      basepath = path.dirname(__file__)
      self.db_path = path.join(basepath, f'../database/server_s.json')
      
      self.load()

  def set_servers(self, a, e):
    self.server_a = a
    self.server_e = e

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
