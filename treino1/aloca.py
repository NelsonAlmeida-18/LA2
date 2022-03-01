"""

Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.

"""

def aloca(prefs):
    alunosSemProjeto=[]
    projetosAlocados=[]
    prefs = sorted(prefs.items(), key=lambda item:item[0])
    for aluno in prefs:
        flag=1
        for i in aluno[1]:
            if i not in projetosAlocados:
                projetosAlocados.append(i)
                flag=0
                break
        if flag:
            alunosSemProjeto.append(aluno[0])
    return alunosSemProjeto