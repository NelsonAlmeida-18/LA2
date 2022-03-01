'''
Neste problema prentede-se que implemente uma função que calcula o rectângulo onde se movimenta um robot.

Inicialmente o robot encontra-se na posição (0,0) virado para cima e irá receber uma sequência de comandos numa string.
Existem quatro tipos de comandos que o robot reconhece:
  'A' - avançar na direcção para o qual está virado
  'E' - virar-se 90º para a esquerda
  'D' - virar-se 90º para a direita 
  'H' - parar e regressar à posição inicial virado para cima
  
Quando o robot recebe o comando 'H' devem ser guardadas as 4 coordenadas (minímo no eixo dos X, mínimo no eixo dos Y, máximo no eixo dos X, máximo no eixo dos Y) que definem o rectângulo 
onde se movimentou desde o início da sequência de comandos ou desde o último comando 'H'.

A função deve retornar a lista de todas os rectangulos (tuplos com 4 inteiros)
'''

def roda(dict, direc):
    if direc=="D":
        if dict["xv"]==1 and dict["yv"]==0:
            dict["xv"]=0
            dict["yv"]=-1
            return dict
        if dict["xv"]==0 and dict["yv"]==1:
            dict["xv"]=1
            dict["yv"]=0
            return dict
        if dict["xv"]==0 and dict["yv"]==-1:
            dict["xv"]=-1
            dict["yv"]=0
            return dict
        if dict["xv"]==-1 and dict["yv"]==0:
            dict["xv"]=0
            dict["yv"]=1
            return dict
    else:
        if dict["xv"]==1 and dict["yv"]==0:
            dict["xv"]=0
            dict["yv"]=1
            return dict
        if dict["xv"]==0 and dict["yv"]==1:
            dict["xv"]=-1
            dict["yv"]=0
            return dict
        if dict["xv"]==0 and dict["yv"]==-1:
            dict["xv"]=1
            dict["yv"]=0
            return dict
        if dict["xv"]==-1 and dict["yv"]==0:
            dict["xv"]=0
            dict["yv"]=-1
            return dict
def robot(comandos):
    listaDasPos=[]
    pos={"x":0,"y":0}
    maxPos={"minX":0,"minY":0,"maxX":0,"maxY":0}
    direct={"xv":0,"yv":1}
    for command in comandos:
        if command =="A":
            pos["x"]+=direct["xv"]
            pos["y"]+=direct["yv"]
            if pos["x"]>maxPos["maxX"]:
                maxPos["maxX"]=pos["x"]
            if pos["x"]<maxPos["minX"]:
                maxPos["minX"]=pos["x"]
            if pos["y"]>maxPos["maxY"]:
                maxPos["maxY"]=pos["y"]
            if pos["y"]<maxPos["minY"]:
                maxPos["minY"]=pos["y"]
        if command=="E":
            direct = roda(direct, "E")
            print(direct)
        if command=="D":
            direct = roda(direct, "D")
            print(direct)
        if command=="H":
            listaDasPos.append((maxPos["minX"],maxPos["minY"],maxPos["maxX"], maxPos["maxY"]))
            pos={"x":0,"y":0}
            maxPos={"minX":0,"minY":0,"maxX":0,"maxY":0}
            direct={"xv":0,"yv":1}
            
    return listaDasPos