def contar_ocorrencias(texto):
    palavras = texto.lower().split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem

texto = "Só sei que nada eu sei"
resultado = contar_ocorrencias(texto)
print("Contagem de ocorrências de cada palavra:")
for palavra, ocorrencias in resultado.items():
    print(f"{palavra}: {ocorrencias}")
