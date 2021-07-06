import os 

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Bacana, Obrigado.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} Bacana, Obrigado.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}Bacana, Obrigado.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} Bacana, Obrigado{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')


def start():
    # Apresentar o chatbot
    print('Olá! Bem-vindo ao Colégio Mackenzie')
    # pedir o nome
    nome = input('Digite seu nome: ')
    # pedir o e-mail
    email = input('Digite seu e-mail: ')
    while True:
        # Oferer o menu de opções
        resposta = input(
            f'Onde você viu o Colégio Mackenzie ?{os.linesep}[1] - Facebook?{os.linesep}[2] - Instagram?{os.linesep}[3] - Google ?{os.linesep}[4] - Recomendação?{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome)


if __name__ == '__main__':
    start()
