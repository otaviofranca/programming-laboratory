'''
9. Escreva um programa que solicita ao usuário para digitar um número inteiro e, em 
seguida, exiba a sequência de Fibonacci até o número digitado.
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

def fibonacci(number):
    fibonacci_seq = [0, 1]

    while fibonacci_seq[-1] + fibonacci_seq[-2] <= number:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])

    return fibonacci_seq

def show_fibonnaci(fibo):
    fibo_seq = fibonacci(fibo)
    
    print("Fibonacci sequence up to", fibo, ":")
    for num in fibo_seq:
        print(num, end=" ")

   
if __name__ == "__main__":
    number = request_number()
    show_fibonnaci(number)
