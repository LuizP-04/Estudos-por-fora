tentativas = 0
palavra = 'paralelepipedo'
resp = ['*'] * len(palavra)

while True:
    letra = input('Qual letra vc quer? ').lower()
    if letra == 'sair':
        break
    for i in range(len(palavra)):
        if letra == palavra[i]:
            resp[i] = letra

    saida = ''
    for i in range(len(resp)):
        saida+=f'{resp[i]}'
    tentativas+=1
    print(f'tentativas: {tentativas}')
    print(saida)
    if saida == palavra:
        print(f'Parabens, você completou o jogo em {tentativas} tentativas, a palavra era {palavra}')
        break