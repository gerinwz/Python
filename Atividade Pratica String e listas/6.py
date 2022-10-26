#6 - Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do 
# mês por extenso.
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
data = input("informe a data de nascimento (dd/mm/aaaa): ")
print ("Você nasceu em ", data.split("/")[0], "de", meses[(int(data.split("/")[1])-1)], "de", data.split("/")[2])
