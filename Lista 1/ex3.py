n  = 1000000
cont = 0
primo = []

for i in range(1,n**0.5):
    cont = 0
    for j in range (2, i):
        if (i % j) == 0:
            cont += 1
    if cont == 0:
        primo.append(i)

print(f"Os números primos são: {primo}")