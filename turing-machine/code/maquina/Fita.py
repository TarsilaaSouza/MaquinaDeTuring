
# codificao dos simbolos

SEM_ESCRITA = '_'
USADO = '*'
ESQUERDA = 'l'
DIREITA = 'r'

class Fita(object):

    def __init__(self, apontador=1, elementos=[]):
        self.apontador=apontador
        self.elementos=elementos

    def get_Fita(self):
        return self.elementos

    def simbolo_topo(self):
        return self.elementos[self.apontador]

    def simbolo_inicial(self):
        return self.apontador

    def inserir(self, entrada):
        self.elementos=[]
        self.elementos.append(SEM_ESCRITA)
        self.elementos += list(input.replace(" ", SEM_ESCRITA))
        self.elementos.append(SEM_ESCRITA)

    def mover(self, direcao):
        if direcao == DIREITA:
            if self.apontador == len(self.elementos) - 1:
                self.elementos.append(SEM_ESCRITA)
                self.apontador += 1
            else:
                self.apontador += 1

        if direcao == ESQUERDA:
            if self.apontador == 0:
                self.elementos = [SEM_ESCRITA] + self.elementos
                self.apontador = 0
            else:
                self.apontador -= 1

    def escrever(self, simbolo):
        if simbolo != USADO:
            self.elementos[self.apontador] = simbolo

    def ponteiro(self):
        indicador = ""
        for e in range(len(self.elementos)):
            if e == apontador:
                indicador += 1
            else:
                indicador += " "
        return indicador

    def info(self):
        return str(self.elementos)

    def strInfo(self):
        return " ".join(self.elementos).replace("_", " ")
