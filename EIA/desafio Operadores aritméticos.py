ovos = 5
pessoas = 2

divisao = 5 / 2
sobra = ovos % pessoas

def frase(valor_ovos):
    if valor_ovos > 1:
        frase = 'ovos'
    else:
        frase = 'ovo'
    return frase

print('Cada pessoa ficou com %d %s de páscoa e sobraram se %d %s'   %(ovos / pessoas, frase(divisao), sobra, frase(sobra)))