from os import path
import json

class CA():

  def __init__(self):
      basepath = path.dirname(__file__)
      self.db_path = path.join(basepath, f'../database/ca.json')
      
      self.load()


  def save(self):
    file = open(self.db_path, 'w')
    file.write(json.dumps({'elections': self.elections, 'users': self.users}, indent=4))
    file.close()

  def load(self):
    if path.isfile(self.db_path):
      file = open(self.db_path, 'r')
      data = json.load(file)
      self.private_key = data['private_key']
      self.public_key = data['public_key']

    else:
      raise Exception('CA.json does not exists')