'''
2. Escreva um programa que solicita ao usuário para digitar dois números inteiros e exiba 
a soma, o produto, a subtração e a divisão desses números na tela.
'''
def validNumber(number):
    while 1:
        if number.isdigit():
            break
        else:
            number = input('Invalid character, please type again!\nTry again: ')
    return int(number)

def requestNum():
    num1 = input('Enter the first Number: ')
    num1 = validNumber(num1)
    num2 = input('Enter the second Number: ')
    num2 = validNumber(num2)
    return num1, num2

def soma(num1, num2):
    return num1 + num2

def produto(num1, num2):
    return num1 * num2

def subtracao(num1, num2):
    return num1 - num2

def divisao(num1, num2):
    return num1 / num2

if __name__ == '__main__':
    print('<<<<< MENU DE OPERAÇÕES >>>>>\n 1 - Soma\n 2 - Produto\n 3 - Subtração\n 4 - Divisão')

    while 1:
        choice = input('Enter your choice: ')

        if choice == '1':
            num1, num2 = requestNum()
            print(f'{num1} + {num2} = {soma(num1, num2)}')
        elif choice == '2':
            num1, num2 = requestNum()
            print(f'{num1} * {num2} = {produto(num1, num2)}')
        elif choice == '3':
            num1, num2 = requestNum()
            print(f'{num1} - {num2} = {subtracao(num1, num2)}')
        elif choice == '4':
            num1, num2 = requestNum()
            if num2 == 0:
                print("Error! Cannot divide by zero.")
            else:
                print(f'{num1} / {num2} = {divisao(num1, num2)}')
        else:
            print("Invalid option!")
