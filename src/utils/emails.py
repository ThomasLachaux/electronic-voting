from mailjet_rest import Client
from os import environ


def send_voter_email(election):
  # Skip if emails are not enabled
  if environ.get('EMAIL_ENABLED') != 'true':
    return

  mailjet = Client(auth=(environ.get('MAILJET_API_KEY'), environ.get('MAILJET_API_SECRET')), version='v3.1')

  messages = []

  for user_id, user in election['users'].items():
    messages.append({
        "From": {
          "Email": "gs15@delachaux.me",
          "Name": "Elections GS15"
        },
        "To": [
          {
            "Email": user['email'],
            "Name": f"{user['firstname']} {user['lastname']}"
          }
        ],
        "Subject": f'Vos identifiants pour l\'election {election["name"]}',
        "TextPart": f"Bonjour {user['firstname']}\n\nFélicitations ! Vous venez d'être inscrit à l'élection {election['name']}.\nVoici la liste des candidates : {', '.join(election['candidates'])}\n\nVoici vos identifiants de votes afin de faire votre devoir d'electeur.\nIdentifiant : {user_id}\nCode secret : {user['c']}\n\nBien cordialement.",
      })

  mailjet.send.create(data={'Messages': messages})
  print('Emails envoyés !')


def send_hash_email(user, election, challenge_hash):
  # Skip if emails are not enabled
  if environ.get('EMAIL_ENABLED') != 'true':
    return

  mailjet = Client(auth=(environ.get('MAILJET_API_KEY'), environ.get('MAILJET_API_SECRET')), version='v3.1')

  messages = []

  messages.append({
      "From": {
        "Email": "gs15@delachaux.me",
        "Name": "Elections GS15"
      },
      "To": [
        {
          "Email": user['email'],
          "Name": f"{user['firstname']} {user['lastname']}"
        }
      ],
      "Subject": f'Confirmation de vote de l\'election {election["name"]}',
      "TextPart": f"Bonjour {user['firstname']}\n\nNous confirmons avoir reçu votre vote. Votre signature de vote est {challenge_hash}, vous pouvez la vérifier à tout moment.\n\nCordialement",
    })

  mailjet.send.create(data={'Messages': messages})
  print('Email de confirmation envoyé')