frase_concatena = ''
while (True):
    palavra = input('Insira um caractere:')
    palavra_1 = palavra
    if palavra == 'esc':
        break
    else:
        frase_concatena += palavra_1
print('Frase concatenada: %s' %(frase_concatena))