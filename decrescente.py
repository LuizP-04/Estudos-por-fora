n = int(input())

for i in range(n):
    a1 = input().split()
    a = int(a1[0])
    b = int(a1[1])
    p1 = input().split()
    if len(p1)!= a:
        print('NO')
        break
    p2 = input()
    if len(p2)!= b:
        print('NO')
        break
    
    maior1 = max(p1)
    maior2 = max(p2)

    if maior1<maior2:
        print('NO')
    else:
        print("YES")