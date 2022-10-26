x = 10
def func():
    global x    #troca o valor de x pelo que está na função (evite variaveis globais)
    x=1
    print(x)
func()
print(x)