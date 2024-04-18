'''
Escreva um programa que solicita ao usuário para digitar uma frase (máximo de 100 
caracteres) e, em seguida, exiba essa frase invertida na tela
'''
def valid_frase(frase):
    while 1:
        if len(frase)<=100:
            return frase
        print('The sentence has exceeded the maximum character length!')
        frase = input('Please try again')
            
def request_frase():
    frase = input('Enter a sentence with a maximum of 100 characters:')
    frase = valid_frase(frase)
    return frase

def inverte_frase(frase):
    frase_invertida = frase[::-1]
    return frase_invertida

if __name__ == "__main__":
    frase = request_frase()
    frase = inverte_frase(frase)
    print('Inverted sentence: ', frase)
