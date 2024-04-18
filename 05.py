'''
Escreva um programa que solicita ao usuário para digitar um número inteiro e, em 
seguida, exiba todos os números pares de 0 até o número digitado
'''
def valid_number(number):
    while 1:
        if number.isdigit():
            break
        else:
            number = input('Invalid character, please type again:')
    return int(number)

def request_number():
    number = input('Enter a number:')
    number = valid_number(number)
    return number

def process_number(number):
    print('List of even numbers:')
    for i in range(number):
        if i % 2 == 0:
            print(f'{i} ', end='')

if __name__ == '__main__':
    number = request_number()
    process_number(number)
