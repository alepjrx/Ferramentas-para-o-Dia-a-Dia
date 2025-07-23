# Envio de SMS com Python e Twilio

Este é um projeto simples em Python para envio de mensagens SMS utilizando a API do Twilio.

O principal objetivo aqui é demonstrar como integrar o serviço de envio de SMS com segurança, utilizando variáveis de ambiente para proteger suas credenciais sensíveis.

---

## Tecnologias Utilizadas

- Python
- Twilio (twilio-python)
- dotenv (python-dotenv)

---

## Segurança com `.env`

As credenciais da API do Twilio (Account SID e Auth Token) não ficam expostas diretamente no código.  
Elas são armazenadas em um arquivo `.env`, que é lido com a biblioteca `python-dotenv`.

Exemplo do `.env`:

DOTENV_TWILIO_ACCOUNT_SID=SEU_SID_AQUI  
DOTENV_TWILIO_AUTH_TOKEN=SEU_TOKEN_AQUI

Nunca envie o arquivo `.env` para o GitHub.  
Adicione no seu `.gitignore`:

.env

---

## Resultado

Uma mensagem SMS é enviada para o número definido no script.

---
