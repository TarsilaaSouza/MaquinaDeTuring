from Estado import Estado

def lerArquivo(caminho):

    try:
        arquivo = open(caminho)
    except IOError:
        break

    SIMBOLO_DE_COMENTARIO = ";"

    estados_gerados = {}

    for linha in arquivo:
        if not linha.startswith(SIMBOLO_DE_COMENTARIO) and not linha.startswith("\n") and len(linha) > 2:
            linha = linha.split(" ")
