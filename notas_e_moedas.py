n100 = 0; n50=0; n20=0; n10=0; n5=0; n2=0; n1=0; m50=0; m25=0; m10=0; m5=0; m1=0

n = float(input())
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
while valortotal>=1:
    valortotal-=1
    n1+=1
while valortotal>=0.5:
    valortotal-=0.5
    m50+=1
while valortotal>=0.25:
    valortotal-=0.25
    m25+=1
while valortotal>=0.1:
    valortotal-=0.1
    m10+=1
while valortotal>=0.05:
    valortotal-=0.05
    m5+=1
while valortotal>0:
    valortotal-=0.01
    m1+=1
    
print(f"NOTAS:\n{n100} nota(s) de R$ 100.00\n{n50} nota(s) de R$ 50.00\n{n20} nota(s) de R$ 20.00\n{n10} nota(s) de R$ 10.00\n{n5} nota(s) de R$ 5.00\n{n2} nota(s) de R$ 2.00\nMOEDAS:\n{n1} moeda(s) de R$ 1.00\n{m50} moeda(s) de R$ 0.50\n{m25} moeda(s) de R$ 0.25\n{m10} moeda(s) de R$ 0.10\n{m5} moeda(s) de R$ 0.05\n{m1} moeda(s) de R$ 0.01")