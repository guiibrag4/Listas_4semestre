# Comentários ao final do exercício, explicando conceitos importantes

def contar_ocorrencias (texto):
    texto = texto.replace (',','').replace ('.', '')
    palavras = texto.lower().split()
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

texto = 'Yo so sie, que nada yo sie heheheh, heheheh, heheheh.'
resultado = contar_ocorrencias(texto)

for palavra, ocorrencia in resultado.items():
    print(f'{palavra}: {ocorrencia}')

# O método lower transforma todas as letras em minúsculas, já o método split divide a string em uma lista

# Replace(old,new,count). Esse método de string em Python é usado para substuir todas as ocorrências de uma sub-string especificada por outra sub-string. A baixo, ta substituindo as vírgulas do texto por um espaço branco. Depois, utilizando novamente, substitui o . por um espaço em branco
    
# Essa variavel contagem inicia um dicionário vazio. Um dicionário em Python é uma coleção não ordenada de itens. Ele possui um par chave:valor. As chaves de um dicionário devem ser únicas e imutáveis. No caso, a chave nesse código é a variável "palavra."
    
# O primeiro for funciona da seguinte forma: Ele percorre cada palavra na lista palavras, que foi criada ao dividr a string texto com o metodo split. A variável palavra então é criada, para que percorra cada palavra da lista, 1 por 1. Para cada palavra na lista palavras, o código verifica se essa palavra já existe como uma chave no dicionário contagem.






































