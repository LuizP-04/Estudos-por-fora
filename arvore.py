class Arvore:

    def __init__(self):
        self.raiz = None
        self.direita = None
        self.esquerda = None
    
    def Adicionar(self,ref, b):
        if self.raiz == None:
            self.raiz = b
        else:
            if b>ref:
                if ref.esquerda == None:
                    ref.esquerda = b
                else:
                    return self.Adicionar(ref.esquerda, b)
            else:
                if ref.direita == None:
                    ref.direita = b
                else:
                    return self.Adicionar(ref.direita, b)
    
    def posordem(self, ref):
        return self.posordem(ref.direita) + self.posordem(ref.esquerda) + str(ref)


n = int(input())
v = 0
while v < n:
    N, S1, S2 = input().split()
    a = Arvore()
    for i in range(len(S1)):
        a.Adicionar(a.raiz, S1[i])

    print(a.posordem(a.raiz))
    
    v+=1