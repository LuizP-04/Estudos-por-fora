n100 = 0; n50=0; n20=0; n10=0; n5=0; n2=0; n1=0

n = int(input())
valortotal = n
while valortotal>=100:
    valortotal-=100
    n100+=1
while valortotal>=50:
    valortotal-=50
    n50+=1
while valortotal>=20:
    valortotal-=20
    n20+=1
while valortotal>=10:
    valortotal-=10
    n10+=1
while valortotal>=5:
    valortotal-=5
    n5+=1
while valortotal>=2:
    valortotal-=2
    n2+=1
while valortotal>0:
    valortotal-=1
    n1+=1

print(f"{n}\n{n100} nota(s) de R$ 100,00\n{n50} nota(s) de R$ 50,00\n{n20} nota(s) de R$ 20,00\n{n10} nota(s) de R$ 10,00\n{n5} nota(s) de R$ 5,00\n{n2} nota(s) de R$ 2,00\n{n1} nota(s) de R$ 1,00")