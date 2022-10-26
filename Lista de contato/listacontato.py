#Crie uma lista de contatos no qual o usuário entra com os valores de:
#•Nome:
#•Telefone:
#•Endereço.
#O usuário pode cadastrar vários contatos. Ao final de cada contato o programa 
#deve perguntar se deseja sair(S/N)
from ast import While
from contextlib import ContextDecorator

contato = dict()
lista = list()

while True:
    contato.clear()
    contato['nome'] = str(input('Nome: '))
    #while True:
    contato['telfone'] = int(input('Telefone:'))
        #if contato ['telefone'] == int(11):
        #        break
        #print ('Erro! Por favor digite apenas numeros')
    contato['endereço'] = str(input('Escreva seu endereço: '))
    lista.append(ContextDecorator.copy())
    while True:
        resp = str(input('Quer Continuar cadastrando? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == "N":
        break

print ('_-' * 30)
print (lista)