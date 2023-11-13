from datetime import datetime

MA = 0
MG = 0
MH = 0

cont = 0
diferenca = 1
parada = 10**-2

def equa(A, B):
    global cont
    global diferenca
    global parada
    global MH
    global MA
    global MG   

    while diferenca > parada:
        
        MH = (2 * A * B) / (A + B)
        MA = (A + B) / 2
        A = MA
        B = MH
        MG = ((A * B) ** 0.5)
        cont += 1
        diferenca = (MA - MH)

for i in range(1,101):
    A = 1
    B = 10 ** i
    diferenca = 1  
    cont = 0

    inicio = datetime.now().microsecond
    equa(A, B)
    fim = datetime.now().microsecond

    print(f"Para B = 10^{i}:")
    print(f"A quantidade de iterações utilizadas foram: {cont}")
    print(f"A média harmônica é: {MH}")
    print(f"A média aritmética é: {MA}")
    print(f"A média geométrica é: {MG}")
    print(f"O tempo de execução foi de {abs(inicio - fim)} microssegundos\n")

