#1 - Faça um programa com uma função chamada somaImposto. 
#A função possui dois parâmetros formais:  taxaImposto, que é a quantia de 
# imposto sobre vendas expressa em porcentagem e custo, que é o custo de um 
# item antes do imposto. A função "altera" o valor de custo para incluir o 
# imposto sobre vendas.

def somaImposto(taxaImposto, Custo):
    return (1 + taxaImposto/100)*Custo
tx_imp = float(input('Digite a porcentagem do imposto: '))
custo_s = float(input('Digite o custo: '))
print('Valor com imposto:', somaImposto(tx_imp,custo_s))