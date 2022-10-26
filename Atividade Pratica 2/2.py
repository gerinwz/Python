import string
nota1= float(input("Digite o valor da primeira nota: "))
nota2= float(input("Digite o valor da segunda nota: "))

soma= float(nota1)+float(nota2)
media = float(soma)/2

print("A nota media é",media)

def new_func(media):
    if float(media) == float(10):
        print("Aprovado com nota maxima")
    elif float(media) >= float(7): 
        print("Aprovado")
    else:
        print("reprovado")
new_func(media)