import random
words = ['HARRY STYLES', 'SANDUICHE', 'CAMINHAO', 'GOLDEN GIRLS', 'SAN FRANSCISCO', 'COMPUTADOR', 'PROGRAMACAO']

choice = random.choice(words)



def LetraExist(letra, palavra):
     for l in palavra:
         if letra == l:
             return True


def NotShownWord(palavra):
    nsw = []
    for r in palavra:
        if r == ' ':
            nsw.append(' ')
        else:
            nsw.append('_ ')
    return nsw


def printNSW(lista):
    for c in lista:
        print(c, end = ' ')

def Acabou(letras):
    a = 0
    for l in letras:
        if l != '_ ':
            a += 1
    if a == len(letras):
         return True
            

letras = NotShownWord(choice)
print(printNSW(letras))



while True:

    if Acabou(letras):
        print('Parabens')
        break

    guess = input('Digite uma letra: ').upper()

    if LetraExist(guess, choice):
        for i, v in enumerate(choice):
            if v == guess:
                letras[i] = v 

    
    print(printNSW(letras))
    print()


