'''
1. Escreva um programa que solicita ao usuário para digitar um número inteiro e, em
seguida, exibe esse número, o dobro e o triplo do valor desse número na tela.
'''
def valid_number(number):
    while 1:
        if number.isdigit():
            break
        else:
            number = input('invalid character, please type again!')    
    return int(number)

def request_number():
    number = input('Enter a number:')
    number = valid_number(number)
    return number    

def process_number(number):
    double_number = number*2
    triple_number = number*3
    return double_number,triple_number

def show_numbers(number1, double, triple):
    print(f'The number entered was: {number1}\nTwice the number is: {double}\nTriple the number is: {triple}')

if __name__ == '__main__':
    number = request_number()
    double_number, triple_number = process_number(number)
    show_numbers(number, double_number, triple_number)