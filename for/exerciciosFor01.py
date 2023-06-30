#range ( * posiçao inicial, ** posição final, *** step's)
texto = input('Insira uma frase: ')
num_caracteres = 0

for letra in texto:
    if letra != ' ':
        num_caracteres += 1
print('A palavra inserida contem %i palavras' %(num_caracteres))