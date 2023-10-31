n  = 10011
n2 = 100
cont = 0
primo = []
total = 0


for i in range(2,n2):
    cont = 0
    for j in range (2, i):
        if (i % j) == 0:
            cont += 1
    if cont == 0:
        primo.append(i)
        total += 1

print(primo)

for j in range(primo):
    cont = 0
    if n % j == 0:
        cont += 1
        print ("Não é primo")
        break
if cont == 0:
    print(f"O valor {n} é primo")



    