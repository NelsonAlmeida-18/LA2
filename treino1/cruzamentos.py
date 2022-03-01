'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que lista os cruzamentos de uma cidade 
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto 
maior o número de ruas que interliga.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos). 
Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

A função deverá retornar uma lista com os nomes dos cruzamentos por ordem crescente de criticidade, 
listando para cada cruzamento um tuplo com o respectivo identificador e o número de ruas que interliga.
Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o mesmo 
nível de criticidade deverão ser listados por ordem alfabética.
'''

def cruzamentos(ruas):
    myDict = {}
    for rua in ruas:
        if rua[0] not in myDict:
            myDict[rua[0]]=0
        if rua[-1] not in myDict:
            myDict[rua[-1]]=0
        if rua[0]==rua[-1]:
            myDict[rua[0]]+=1
            continue
        if rua[0] in myDict:
            myDict[rua[0]]+=1
        if rua[-1] in myDict:
            myDict[rua[-1]]+=1
    newDict=sorted(myDict.items(),key=lambda item:item[0])
    newDict=sorted(newDict, key=lambda item:item[1])
    return newDict



