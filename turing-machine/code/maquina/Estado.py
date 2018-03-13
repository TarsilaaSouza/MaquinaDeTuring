

class Estado(object):

    def __init__(self, nome="", simbolo="", novo_simbolo="", direcao="", proximo_estado=""):
        self.nome=nome
        self.simbolo=simbolo
        self.novo_simbolo=novo_simbolo
        self.direcao=direcao
        self.proximo_estado=proximo_estado

    def set_estado(self, nome="", simbolo="", novo_simbolo="", direcao="", proximo_estado=""):
        self.nome=nome
        self.simbolo=simbolo
        self.novo_simbolo=novo_simbolo
        self.direcao=direcao
        self.proximo_estado=proximo_estado

    def strInfo(self):
        return "Estado atual %s" % self.nome

    def info(self):
        return "%s %s %s %s" % (self.nome, self.simbolo, self.novo_simbolo, self.direcao, self.proximo_estado)
