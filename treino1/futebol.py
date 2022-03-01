'''

Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com 
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.

'''
def somadora(tuplo, valores):
    (pontos, golosMarcados, golosSofridos)=tuplo
    (pontosAdicionar, maisgolos, maisgolosS)=valores
    return(pontos+pontosAdicionar, golosMarcados+maisgolos, golosSofridos+maisgolosS)

def tabela(jogos):
    joguinhos = {}
    for (equipa1, golos1, equipa2, golos2) in jogos:
        if equipa1 not in joguinhos:
            joguinhos[equipa1]=(0,0,0)
        if equipa2 not in joguinhos:
            joguinhos[equipa2]=(0,0,0)
        if golos1>golos2:
            joguinhos[equipa1]=somadora(joguinhos[equipa1],(3, golos1, golos2))
            joguinhos[equipa2]=somadora(joguinhos[equipa2],(0, golos2, golos1))
        if golos1==golos2:
            joguinhos[equipa1]=somadora(joguinhos[equipa1],(1, golos1, golos2))
            joguinhos[equipa2]=somadora(joguinhos[equipa2],(1, golos2, golos1))
        if golos2>golos1:
            joguinhos[equipa1]=somadora(joguinhos[equipa1],(0, golos1, golos2))
            joguinhos[equipa2]=somadora(joguinhos[equipa2],(3, golos2, golos1))
    joguinhos = sorted(joguinhos.items())
    joguinhos = sorted(joguinhos, key=lambda item:(item[1][2]-item[1][1]))
    joguinhos = sorted(joguinhos, key=lambda item:item[1][0], reverse=True)
    joguinhos = [(equipa, pontos) for (equipa,(pontos, x,y)) in joguinhos]
    return joguinhos