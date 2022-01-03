from PyInquirer import prompt
import utils.elgamal
import utils.zero_knowledge_proof
import random
from servers import serverA
from servers import serverE
from servers import serverS

# TODO test à virer

pubkey = 9646224207782033553525015639298134527232697951858462768120449435918300343624398631197849149595927330211704344941369918536389067336844642012528532377250617349299628141885415827083368536845215078196952875216808983529360415056792985468503288047795853887851388870034503760833753483240624029815645029981075384136299177434908199300556336793335062584886281803128793264229441053683056459811635355197604126775728201725828001271167593584815474767796105400193007830296710944330736992391797800643773046961312585784569213918522330709923322793606068358222659739591012063066299904329701717501436815754228659619656088611505846846545

# resp, chal = utils.zero_knowledge_proof.prove(g,p,"995ae4fc-6a57-4383-b586-258aa0a43865")
# print(utils.zero_knowledge_proof.verify(g, p, resp, pubkey, chal))

questions = {
  'type': 'list',
  'name': 'menu',
  'message': 'Bonjour ô maître Rémi ! Comme puis-je aider votre Sainteté ?',
  'choices': [
    {'name': 'Créer une élection', 'value': 'create_election'},
    {'name': 'Créer un electeur', 'value': 'create_elector'},
    {'name': 'Créer un vote', 'value': 'create_vote'},
    {'name': 'Vérifier un vote', 'value': 'check_vote'},
    {'name': 'Procéder au dépouillement', 'value': 'proceed_counting'},
    {'name': 'Supprimer des données', 'value': 'delete_data'},
    {'name': 'Quitter', 'value': 'quit'}
  ]
}

a = serverA.serverA()
e = serverE.serverE()
s = serverS.serverS()

a.set_servers(e, s)
e.set_servers(a, s)
s.set_servers(a, e)

while True:
  answer = prompt(questions)['menu']

  if answer == 'quit':
    break

  submenu = __import__(f"menu.{answer}", fromlist=[None])
  submenu.entrypoint(a, e, s) 

print('Au revoir')