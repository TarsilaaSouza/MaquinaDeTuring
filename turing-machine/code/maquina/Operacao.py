from Estado import Estado

#codificao

UTILIZADO = '*'
SIMBOLO_DE_COMENTARIO = ';'

class Operacao(object):

    def __init__(self):
        self.estados = {}

    def existEstado(self):
        return bool(self.estados)

    def inserirEstado(self, estado=Estado()):
        self.estados=[(estado.nome, estado.simbolo)] = estado

    def setEstados(self, estados):
        self.estados.clear()
        self.estados = estados

    def proxEstado(self, nome, simbolo):
        proximo = self.estados.get((nome, simbolo))
        if proximo is None:
            proximo = self.estados.get((nome, UTILIZADO))
        return proximo

    def stringInfo(self):
        return str(self.estados.keys())

    def info(self):
        return "Operacao"
