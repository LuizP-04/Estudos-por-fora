n=int(input())
for i in range(n):
    palavra = input()
    if len(palavra)<3:
        print('i')
    else:
        palavrare = palavra[:-2]
        palavrare+='i'
        print(palavrare)