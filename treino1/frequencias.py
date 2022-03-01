'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''

def frequencia(texto):
    freqs = {}
    texto = texto.split(" ")
    for palavra in texto:
        if palavra not in freqs:
            freqs[palavra]=1
        else:
            freqs[palavra]+=1
    freqs=sorted(freqs.items(), key = lambda item:item[0])
    freqs=sorted(freqs, key = lambda item:item[1], reverse=True)
    freqs=[x for x,y in freqs]
    return freqs