while True:
    try:
        passou = 0
        q = int(input())
        grid = []
        a = input().split()
        for i in range(len(a)):
            a[i] = int(a[i])
            grid.append(a[i])
        chegada = []
        b = input().split()
        for i in range(len(b)):
            b[i] = int(b[i])
            chegada.append(b[i])
        passar = ['0']*q
        for i in range(q):
            v = chegada[i]-1
            passar[v] = '1'
            for j in range(q):
                if v == grid[j]-1:
                    break
                else:
                    if passar[grid[j]-1] == '0':
                        passou+=1
                

        print(passou)
    except EOFError:
        break