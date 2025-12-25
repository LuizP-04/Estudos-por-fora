n = int(input())
v = 0
while v < n:
    diamante = 0
    linha = input()
    pilha = []
    lista = []
    for i in range(len(linha)):
        if linha[i] == '<':
            lista.append(linha[i])
        elif linha[i] == '>':
            pilha.append(linha[i])
            if len(lista) != 0:
                del lista[0]
                pilha.pop()
                diamante+=1

    print(diamante)

    v+=1