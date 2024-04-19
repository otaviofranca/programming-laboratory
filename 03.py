'''
3. Escreva um programa que solicita ao usuário para digitar um número real e, em 
seguida, exiba esse número, o dobro e o triplo do valor desse número na tela.
'''
def valid_number(number):
    while 1:
        try:
            number = float(number)
            break
        except ValueError:
            number = input('Invalid input, please enter a numeric value: ')
    return number

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