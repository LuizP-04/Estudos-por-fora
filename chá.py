tc = input()
guess = input().split()
ra = 0
for i in range(len(guess)):
    if guess[i] == tc:
        ra+=1

print(ra)