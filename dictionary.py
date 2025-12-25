frase = 'O Python é uma linguagem de programação ' \
'multiparidigma.' \
'Python foi criada por Guido van Rossum'.lower()

dic = {}
for i in range(len(frase)):
    if frase[i] == ' ':
        pass
    elif frase[i] not in dic:
        dic[frase[i]] = 1
    else:
        dic[frase[i]] += 1


apareceu_mais = max(dic.values())

for i in dic:
    if dic[i] == apareceu_mais:
        print(dic.keys())
    else:
        pass