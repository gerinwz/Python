#3 - Escreva um programa que recebe três inteiros como entrada do teclado e 
# escreva na tela a média, a soma, o produto, o menor valor e o maior valor, 
# usando uma linha para cada resultado.

a = int(input("Digite o primeiro valor:"))
b = int(input("Digite o segundo valor:"))
c = int(input("Digite o terceiro valor:"))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c

soma = a + b + c 
media = soma /3

print (f"O valor da Media é: {int(media)}")
print (f"A soma dos 3 numeros são: {soma}")
print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")