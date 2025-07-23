import os
from twilio.rest import Client
from dotenv import load_dotenv


#1
load_dotenv()
twilio_account_sid = os.getenv('DOTENV_TWILIO_ACCOUNT_SID')
twilio_auth_token = os.getenv('DOTENV_TWILIO_AUTH_TOKEN')


#2
account_sid = twilio_account_sid
auth_token = twilio_auth_token
client = Client(account_sid, auth_token)


#3
message = client.messages.create(
    body='Insira o texto do seu SMS aqui',
    from_='insira o telefone que irá enviar a mensagem, ex:+55 DDD XXXXX-XXXX',
    to='insira o telefone que irá receber a mensagem, ex:+55 DDD XXXXX-XXXX'
)