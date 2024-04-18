'''
4. Escreva um programa que solicita ao usuário para digitar seu nome e, em seguida,
exiba uma saudação personalizada (“Bem vindo xxx") na tela informando quantos
caracteres tem o nome digitado.

'''
def request_Name():
    name = input('Hello, Enter your name:')
    return name
def show_Menu(name):
    print(f'Welcome {name}\nYour name has {len(name)} characters.')
if __name__ == '__main__':
    name =request_Name()
    show_Menu(name)