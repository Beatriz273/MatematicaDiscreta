
    
MH = 0
MG = 0
MA = 0
A = 1
B = 10

cont = 0
diferenca = 1
parada = 10**-2

while diferenca > parada:
    MH = (2*A*B) / (A+B)
    MA = (A+B)/2
    A = MA
    B = MH
    MG = ((A*B)**0.5)
    cont += 1
    diferenca = MA - MH
       
        



print (f"A quantidade de interações utilizadas foram: {cont} ")
print (f"A média harmônica é: {MH}")
print (f"A média aritmética é: {MG}")
print (f"A média geométrica é: {MA}")
