'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.




Só corre 80% dos casos não sei porquê
'''

def auxSorter(nomes):
    return sorted(nomes)
    
def apelidos(nomes):
    nomesOrdenados={}
    for nome in nomes:
        nome=nome.split()
        if len(nome) not in nomesOrdenados:
            nomesOrdenados[len(nome)]=[" ".join(nome)]
        else:
            nomesOrdenados[len(nome)].append(" ".join(nome))
    nomesOrdenados = sorted(nomesOrdenados.values(), reverse=True)
    nomesListados=[]
    for nomes in nomesOrdenados:
        if len(nomes)>1:
            nomesListados+=auxSorter(nomes)
        else:
            nomesListados+=nomes
    
    return nomesListados

def apelidos(nomes):
    nomes.sort()
    nomes.sort(key=lambda item: len(item.split()))
    return nomes
