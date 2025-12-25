vezes = int(input())
a = 0
count = [[0]*vezes]
while a != vezes:
    array = input().split()
    array = list(array) 
    for i in range(len(array)-1):
        for j in range(i+1):
            if array[i] == array[j+1]:
                count[a]+=1

print(count)