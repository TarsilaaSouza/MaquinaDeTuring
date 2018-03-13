
# codificao dos simbolos

SEM_ESCRITA = '_'
USADO = '*'
ESQUERDA = 'l'
DIREITA = 'r'

class Fita(object):

    def __init__(self, posicao_inicio=1, elementos=[]):
        self.posicao_inicio=posicao_inicio
        self.elementos=elementos

    def get_Fita(self):
        return self.elementos

    def simbolo_topo(self):
        return self.elementos[self.posicao_inicio]

    def simbolo_inicial(self):
        return self.posicao_inicio

    def inserir(self, entrada):
        self.elementos=[]
        self.elementos.append(SEM_ESCRITA)
        self.elementos += list(input.replace(" ", SEM_ESCRITA))
        self.elementos.append(SEM_ESCRITA)
