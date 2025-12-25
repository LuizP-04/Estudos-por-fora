while True:
    ondas = 0
    q = int(input())
    if q == 0:
        break
    a = [0]*q
    entrada = input().split()
    for i in range(q):
        a[i] = abs(int(entrada[i]))
    for i in range(q):
        if a[i]!=0:
            ondas+=1
            for j in range(q):
                if a[j] == a[i]:
                    if int(entrada[j]) != a[i]:
                        ondas-=1
                        break
    print(ondas)