"""

Implemente uma função que calcula o horário de uma turma de alunos.
A função recebe dois dicionários, o primeiro associa a cada UC o
respectivo horário (um triplo com dia da semana, hora de início e
duração) e o segundo associa a cada aluno o conjunto das UCs em
que está inscrito. A função deve devolver uma lista com os alunos que
conseguem frequentar todas as UCs em que estão inscritos, indicando
para cada um desses alunos o respecto número e o número total de horas
semanais de aulas. Esta lista deve estar ordenada por ordem decrescente
de horas e, para horas idênticas, por ordem crescente de número.

"""

def horario(ucs,alunos):
    ucs = dict(sorted(ucs.items(), key = lambda item:item[0]))
    whiteListed=[]
    for aluno in alunos:
        horario={}
        tempoDeAulas=0
        flag=0
        for uc in alunos[aluno]:
            if uc not in ucs:
                flag=1
            else:
                dia,horaInit,tempoAulas=ucs[uc]
                tempoDeAulas+=tempoAulas
                while(tempoAulas)!=0:
                    if (dia,horaInit) not in horario:
                        horario[dia,horaInit]=uc
                    else:
                        flag=1
                    horaInit+=1
                    tempoAulas-=1
        if flag==0:
            whiteListed.append((aluno,tempoDeAulas))
    whiteListed=sorted(whiteListed, key=lambda item:item[0])
    whiteListed=sorted(whiteListed, key=lambda item:item[1], reverse=True)
    return whiteListed