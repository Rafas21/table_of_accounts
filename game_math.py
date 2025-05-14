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
    print()
    
    while True:
        choice = input("Digite o número da operação desejada: ")
        print()
        operations = {'1': '+', '2': '-', '3': '*', '4': '/'}
        if choice in operations:
            return operations[choice]
        print("Opção inválida. Escolha entre 1 e 4.")

def gerar_pergunta(operacao):

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    if operacao == '/':
        num1 = num1 * num2 

    print(f'{num1} {operacao} {num2} = ?')
    print()
    return num1, num2

def obter_resposta_usuario():

    response = input('Digite a resposta: ')
    try:
        print()
        return float(response)
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

    operation = escolher_operacao()

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


    correct_answers = 0

    for _ in range(total):
        num1, num2 = gerar_pergunta(operation)
        response_user = obter_resposta_usuario()

        if response_user is None:
            limpar_tela()
            continue

        correct_answer = calcular_resposta(num1, num2, operation)

        if abs(response_user - correct_answer) < 0.01:
            print("Resposta correta!")
            correct_answers += 1
        else:
            print(f"Resposta incorreta! A resposta correta é {correct_answer:.2f}")
        print()

    print(f'Você acertou {correct_answers} de {total} questões!')

def perguntar_se_deseja_sair():

    while True:
        choice = input('Deseja sair? [s]im ou [n]ão: ').strip().lower()
        if choice.startswith('s'):
            return True
        elif choice.startswith('n'):
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