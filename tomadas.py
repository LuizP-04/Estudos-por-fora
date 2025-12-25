tomadas = input().split()
for i in range(len(tomadas)):
    tomadas[i] = int(tomadas[i])
tomadas[-1]+=1
tt = 0
for i in range(len(tomadas)):
    if tomadas[i] < 0:
        break
    elif tomadas[i] == 1:
        pass
    else:
        tt+=(tomadas[i]-1)

print(tt)