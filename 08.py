'''
8. Escreva um programa que solicita ao usuário para digitar um número inteiro e, em
seguida, exiba o fatorial desse número.
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

def calcular_fatorial(number):
    if number < 0:
        return "It is not possible to calculate the factorial of a negative number :("

    elif number == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, number + 1):
            fatorial *= i
        return fatorial

if __name__ == "__main__":
    number = request_number()
    resultado = calcular_fatorial(number)
    print("The factorial of", number, "is:", resultado)
