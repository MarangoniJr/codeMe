contador = 0
media = 0

while (contador < 5):
    valores = int(input('Insira um número: '))
    media += valores
    contador += 1
print('A média entre os valores digitados é de %2.f' %(media / 5))