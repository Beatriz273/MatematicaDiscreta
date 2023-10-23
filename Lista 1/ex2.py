#Ver se o número é primo

inicio = int(input("Insira o início do intervalo: "))
fim = int(input("Insira o fim do intervalo: "))
v = []
cont = 0 

for i in range(inicio, fim+1):
    cont = 0
    for j in range(2, i):
        if (i % j == 0):
            cont +=1
    if cont == 0:
        v.append(i)

print(v)