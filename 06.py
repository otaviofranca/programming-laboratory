'''
Escreva um programa que solicita ao usuário para digitar um número inteiro e, em 
seguida, exiba a soma de todos os números ímpares de 1 até o número digitado
'''
def valid_number(number):
    while True:
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
    odd_sum = 0
    print('List of odd numbers:')
    for i in range(1, number + 1):
        if i % 2 == 1:
            print(f'{i} ', end='')

if __name__ == '__main__':
    number = request_number()
    process_number(number)
