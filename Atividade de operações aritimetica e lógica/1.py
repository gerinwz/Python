#1 - Analise o programa abaixo e, para cada uma das saídas (comandos print), 
# detalhe passo a passo como o Python (segundo suas prioridades) resolveria as 
# equações e o resultado final obtido.
x = 2
y = 3
z = 0.5
print(x + x * x ** (y * x) / z)
print(not x + z < y or x + x * z >= y and True)

#1º - print(x + x * x ** --(y * x)-- / z)
#                             /\ primeira leitura
#2º - print(x + x * --x ** (y * x)-- / z)
#                     /\ segunda leitura expoente
#3º - print(x + --x * x ** (y * x) / z--)
#                   /\ primeira a multiplicação depois a divisão
#4º - print--(x + x * x ** (y * x) / z)--
#             /\ finalizando a conta coma  soma

# print(not x + z < y or x + x * z >= y and True)
#not 2 + 0.5 < 3 or 2 + 2 * 0.5 >= 3 and True =>
#not 2 + 0.5 < 3 or 2 + 1 >= 3 and True =>
#not 2.5 < 3 or 2 + 1 >= 3 and True =>
#not 2.5 < 3 or 3 >= 3 and True =>
#not True or 3 >= 3 and True =>
#not True or True and True =>
#False or True and True =>
#False or True =>
#True