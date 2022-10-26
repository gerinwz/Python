from ast import Num
quant = média = maior = menor = 0
while quant < 3:
    núm = int(input('Digite um número:'))
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
print ('O maior valor foi {} e o menor foi {}'.format(maior, menor))
