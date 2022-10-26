# 7 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
list_n = []
print ('Informe os 10 numeros Reais')
for i in range (10):
    list_n.append(float(input('Numero '+ str(i+1) + ': ')))
list_n.reverse()
#list_n.sort(reverse=True)
print(list_n)