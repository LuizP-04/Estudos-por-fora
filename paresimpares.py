n = int(input())
v = 0
tempo = 0
pares = []
impares = []
while v < n:
    numero = int(input())
    if numero%2==0:
        pares.append(numero)
    else:
        impares.append(numero)
    v+=1
pares.sort()
for i in range(len(pares)):
    print(pares[i], end='\n')
impares.sort(reverse=True)
for i in range(len(impares)):
    print(impares[i], end='\n')