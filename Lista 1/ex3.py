n  = 50
cont = 0

for i in range(1,n):
    cont = 0
    for j in range (2, i):
        if (i % j) == 0:
            cont += 1
    if cont == 0:
        print(f"{i} é primo")