texto = input('Insira uma frase:')
contador = 0
espaco_branco = 0
while(contador < len(texto)):
    if(texto[contador] == ' '):
        espaco_branco += 1
    contador += 1
print('A palavra inserida contem %i espaços em branco!' %(espaco_branco))