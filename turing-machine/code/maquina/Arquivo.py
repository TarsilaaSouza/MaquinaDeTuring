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
            linha[-1] = linha[-1].strip("\n")
            estado_gerado = Estado(linha[0], linha[1], linha[2], linha[3], linha[4])
            estados_gerados[(estado_gerado.nome, estado_gerado.simbolo)] = estado_gerado

    arquivo.close()

    return estados_gerados
