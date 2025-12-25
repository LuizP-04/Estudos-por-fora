def fatorial(a):
    if a == 1:
        return 1
    else:
        return a * fatorial(a-1)

n = int(input())
print(fatorial(n))