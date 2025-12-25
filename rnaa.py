linha = input().lower()
rnaa = 0
for i in range(len(linha)-1):
    if linha[i] == 'b' and linha[i+1] =='s':
        rnaa+=1
        i+=2
    elif linha[i] == 's' and linha[i+1] =='b':
        rnaa+=1
        i+=2
    elif linha[i] == 'f' and linha[i+1] =='c':
        rnaa+=1
        i+=2
    elif linha[i] == 'c' and linha[i+1] =='f':
        rnaa+=1
        i+=2
    else:
        pass

print(rnaa)