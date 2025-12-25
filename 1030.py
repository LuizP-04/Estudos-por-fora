n = int(input())
c1 = 0
while n > c1:
    d1, d2 = map(int, input().split())
    lista = []
    for i in range(d1):
        lista.append(i+1)
    contagem = 1
    while len(lista)!=1:
        lista_d = []
        for i in range(len(lista)):
            if contagem%d2==0:
                lista_d.append(i)
                contagem+=1
            else:
                contagem+=1

        for c in range(len(lista_d)):
            if lista_d[c]<len(lista):
                lista.pop(lista_d[c])
    
    print(lista[0])
    c1+=1