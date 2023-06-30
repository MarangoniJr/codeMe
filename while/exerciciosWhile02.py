contador = 0
soma = 0

while(contador < 5):
    contador += 1
    valores = int(input('Insira um número: '))
    if valores < 0:
        continue
    soma += valores
print('A Soma dos numeros inseridos é de %d' %(soma))