Criador de QR Code em Python
----------------------------

Descrição:

Script em Python para criar QR Codes personalizados.
Permite escolher a pasta de destino antes de gerar o primeiro QR Code.
Os arquivos gerados são salvos com o nome escolhido + data no formato dd_mm_aa.

Funcionalidades:

- Gera QR Codes a partir de texto ou links.
- Permite definir a pasta de saída.
- Nome do arquivo inclui a data automaticamente.
- Escolha de cores para frente e fundo do QR Code.

Requisitos:

- Python 3.x
- Biblioteca qrcode
- Biblioteca Pillow

Instalação:

1. Clone este repositório
2. Instale as dependências:
   pip3 install -r requirements.txt

Uso:

1. Execute o script:
python main.py
2. Informe o caminho da pasta onde deseja salvar os QR Codes.
3. Digite o texto ou link.
4. Informe o nome do arquivo (sem extensão).
5. O QR Code será gerado e salvo na pasta escolhida.

Exemplo:

Entrada:

Pasta destino: /Users/usuario/Desktop/MeusQRCodes

Texto/Link: https://www.google.com

Nome do arquivo: google

Saída: "google_(02_08_25).png" salvo em /Users/usuario/Desktop/MeusQRCodes
