"""
Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a 
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números 
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""
def aux(cards):
    string = list(cards[0])
    for card in cards[1:]:
        pos=0
        leng= len(card)
        while(pos<leng):
            if card[pos]!=string[pos] and card[pos]!="*":
                string[pos]=card[pos]
            pos+=1
    return "".join(string)

def hacker(log):
    myDict={}
    for card,nome in log:
        if nome not in myDict:
            myDict[nome]=[]
        myDict[nome].append(card)
    listing = []
    for person in myDict:
        listing.append((aux(myDict[person]), person))
    
    temp = sorted(listing, key=lambda item:item[1])
    return(sorted(temp, key=lambda item:len(item[0])-item[0].count("*"), reverse=True))