numero = int(input('Insira um número: '))
for i in range(numero-1, 1, -1):
    numero *= i
print('Fatorial do número inserido éh: %i' %(numero))