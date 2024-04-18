'''
1. Escreva um programa que solicita ao usuário para digitar um número inteiro e, em
seguida, exibe esse número, o dobro e o triplo do valor desse número na tela.
'''
       
def request_number():
    while 1:
        number = input('\nEnter a number:')
        if number.isdigit():
            break
        else:
            print('invalid character, please type again!')
    return int(number)

def process_number(number):
    double_number = number*number
    triple_number = double_number*number
    return double_number,triple_number

def show_numbers(number1, double, triple):
    print(f'The number entered was: {number1}\nTwice the number is: {double}\nTriple the number is: {triple}')

if __name__ == '__main__':
    number = request_number()
    double_number, triple_number = process_number(number)
    show_numbers(number, double_number, triple_number)