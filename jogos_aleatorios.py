import random

lista = [random.randint(1,60) for i in range(6)]
lista2 = [random.randint(1,60) for i in range(6)]
lista.sort()
lista2.sort()
print(lista, lista2)