from PyInquirer import prompt

questions = {
  'type': 'list',
  'name': 'menu',
  'message': 'Bonjour ô maître Rémi ! Comme puis-je aider votre Sainteté ?',
  'choices': [
    {'name': 'Créer un vote', 'value': 'create_vote'},
    {'name': 'Enregistrer un electeur', 'value': 'register_elector'},
    {'name': 'Enregistrer un vote', 'value': 'register_vote'},
    {'name': 'Vérifier un vote', 'value': 'check_vote'},
    {'name': 'Procéder au dépouillement', 'value': 'proceed_counting'}
  ]
}

answer = prompt(questions)

submenu = __import__(f"menu.{answer['menu']}", fromlist=[None])
submenu.entrypoint() 