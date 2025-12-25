n = int(input())
a=0; m=0

while n > 30:
    n-=30
    m+=1
    if m>12:
        a+=1
        m-=12    

print(f"{a} ano(s)\n{m} mes(es)\n{n} dia(s)\n")
