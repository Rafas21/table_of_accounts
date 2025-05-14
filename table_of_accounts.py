import random
import os

def limpar_tela():

    os.system('cls')

def escolher_operacao():

    print("Escolha a operação:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    
    while True:
        escolha = input("Digite o número da operação desejada: ")
        operacoes = {'1': '+', '2': '-', '3': '*', '4': '/'}
        if escolha in operacoes:
            return operacoes[escolha]
        print("Opção inválida. Escolha entre 1 e 4.")

def gerar_pergunta(operacao):

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    if operacao == '/':
        num1 = num1 * num2 

    print(f'{num1} {operacao} {num2} = ?')
    return num1, num2

def obter_resposta_usuario():

    resposta = input('Digite a resposta: ')
    try:
        return float(resposta)
    except ValueError:
        print('Entrada inválida! Digite um número.')
        return None

def calcular_resposta(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2

def jogar_rodada():

    operacao = escolher_operacao()

    while True:
        try:
            total = int(input('Quantas questões você quer responder?: '))
            if total < 0:
                print("Digite um número zero ou maior.")
                continue
            elif total == 0:
                print("Rodada pulada.")
                return
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


    acertos = 0

    for _ in range(total):
        num1, num2 = gerar_pergunta(operacao)
        resposta_usuario = obter_resposta_usuario()

        if resposta_usuario is None:
            limpar_tela()
            continue

        resposta_correta = calcular_resposta(num1, num2, operacao)

        if abs(resposta_usuario - resposta_correta) < 0.01:
            print("Resposta correta!")
            acertos += 1
        else:
            print(f"Resposta incorreta! A resposta correta é {resposta_correta:.2f}")
        print()

        print(f'Você acertou {acertos} de {total} questões!')

def perguntar_se_deseja_sair():

    while True:
        escolha = input('Deseja sair? [s]im ou [n]ão: ').strip().lower()
        if escolha.startswith('s'):
            return True
        elif escolha.startswith('n'):
            limpar_tela()
            return False
        else:
            print('Entrada inválida! Digite "sim" ou "não".')
            limpar_tela()

def main():

    while True:
        jogar_rodada()
        if perguntar_se_deseja_sair() == True:
            break
        else:
            continue

main()