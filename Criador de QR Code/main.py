import qrcode
import os
from datetime import datetime

def escolher_pasta_destino():
    #pergunta pro usuario onde salvar os qrcodes criados, achei melhor assim
    while True:
        caminho = input('Digite o caminho da pasta onde salvar os QR Codes: ')

        #se o caminho for relativo, transformar em absoluto:
        caminho = os.path.abspath(os.path.expanduser(caminho))

        #criar a pasta se não existir
        try:
            os.makedirs(caminho, exist_ok=True)
            print(f'Pasta definida para: {caminho}')
            return caminho
        except Exception as e:
            print(f'Erro ao criar pasta: {e}')
            print('Tente novamente')

def criar_qrcode(pasta_destino):
    #criar pasta pra salvar os qr code que forem criados
    pasta_destino = pasta_destino_global
    os.makedirs(pasta_destino, exist_ok=True) #cria a pasta se não existir

    #pegar os dados
    data = input('Digite o texto ou link para gerar o QR Code: ').strip()
    nome_arquivo = input('Digite o nome do arquivo (sem extensão): ').strip()

    #pegar data atual no formato dd_mm_aa
    data_atual = datetime.now().strftime('%d_%m_%y')

    #juntar a data no nome
    nome_arquivo = f'{nome_arquivo}_({data_atual})'

    #garantir que o arquivo seja .png
    if not nome_arquivo.endswith('.png'):
        nome_arquivo += '.png' #essa aqui foi boa

    #caminho do arquivo
    caminho_arquivo = os.path.join(pasta_destino, nome_arquivo) #esse os.path.join garante que funciona em macos, win e linux

    #criar o QR Code
    qr = qrcode.QRCode(
        version=1, #tamanho (de 1 a 40, 1 é o menor)
        error_correction=qrcode.constants.ERROR_CORRECT_L, #nível de correção
        box_size=10, #tamanho de cada quadrado
        border=4, #borda em "caixinhas"
    )

    qr.add_data(data)
    qr.make(fit=True)

    #criar a imagem
    img = qr.make_image(fill_color='#4f4f4f', back_color='#D3D3D3')

    #salvar a imagem
    img.save(caminho_arquivo)
    print(f'QR Code criado e salvo como "{nome_arquivo}" na pasta "{pasta_destino}"')

#perguntar pasta apenas uma vez
pasta_destino_global = escolher_pasta_destino()

while True:
    criar_qrcode(pasta_destino_global)
    continuar = input('Deseja criar outro QR Code? (s/n): ').strip().lower()
    if continuar != 's':
        print('Encerrando o programa...')
        break