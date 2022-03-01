'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos. 
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos, 
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''

def isbn(livros):
    livrosInvalidos={}
    for livro in livros:
        digit = 0
        pos=0
        livrinho = livros[livro]
        while(pos<len(livrinho)):
            if pos%2!=0:
                digit+=int(livrinho[pos])*3
            else:
                digit+=int(livrinho[pos])
            pos+=1
        if digit%10!=0:
            livrosInvalidos[livro]=livros[livro]
    return sorted(livrosInvalidos)