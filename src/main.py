from PyInquirer import prompt
import utils.elgamal
import random

# TODO test à virer
p = 32317006071311007300338913926423828248817941241140239112842009751400741706634354222619689417363569347117901737909704191754605873209195028853758986185622153212175412514901774520270235796078236248884246189477587641105928646099411723245426622522193230540919037680524235519125679715870117001058055877651038861847280257976054903569732561526167081339361799541336476559160368317896729073178384589680639671900977202194168647225871031411336429319536193471636533209717077448227988588565369208645296636077250268955505928362751121174096972998068410554359584866583291642136218231078990999448652468262416972035911852507045361090559
g = 2
message = 333
s = random.randint(1, p)
pubkey = utils.math.exponentiation(g, s, p)

c1, c2 = utils.elgamal.encrypt(message, pubkey, p, g)
m = utils.elgamal.decrypt(c1, c2, p, s)

print(m)

questions = {
  'type': 'list',
  'name': 'menu',
  'message': 'Bonjour ô maître Rémi ! Comme puis-je aider votre Sainteté ?',
  'choices': [
    {'name': 'Créer une élection', 'value': 'create_election'},
    {'name': 'Créer un electeur', 'value': 'create_elector'},
    {'name': 'Créer un vote', 'value': 'create_vote'},
    {'name': 'Vérifier un vote', 'value': 'check_vote'},
    {'name': 'Procéder au dépouillement', 'value': 'proceed_counting'}
  ]
}

# answer = prompt(questions)

# submenu = __import__(f"menu.{answer['menu']}", fromlist=[None])
# submenu.entrypoint() 