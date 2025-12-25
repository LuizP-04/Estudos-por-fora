n = int(input())

for i in range(n):
    count = 1
    palavra = input()
    for l in range(len(palavra)-1):
        if palavra[l] != palavra[l+1]:
            count+=1
    if count==0:
        count+=1
    print(count)
