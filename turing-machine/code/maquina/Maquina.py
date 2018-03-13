from Arquivo import Arquivo
from Operacao import Operacao
from Fita import Fita

 #codificao dos simbolos

ESTADO_INICIAL = '0'
ACEITACAO = 'halt-accept'
REJEICAO = 'halt-reject'

class Maquina:

    def __init__(self, Fita=Fita(), Operacao=Operacao()):
        self.Fita = Fita
        self.Operacao = Operacao

    def existPrograma(self):
        return self.Operacao.existEstado()

    def carregamento(self, caminhoDoArquivo):
        estados = Arquivo(caminhoDoArquivo)
        self.Operacao.setEstados(estados)

    def inserirFita(self, entrada_fita):
        self.Fita.inserirFita(entrada_fita)

    def print_info_atual(self, Fita, estado_atual_nome, qtdPassos):
        print("Estado atual: %s - Posicao: %d - Passos: %d" % (estado_atual_nome, Fita.simbolo_topo, qtdPassos))

    def startMaquina(self):

        qtdPassos = 0
        estado_atual = self.Operacao.proxEstado(ESTADO_INICIAL, self.Fita.simbolo_topo)

        while True:

            if estado_atual is not None:
                self.print_info_atual(self.Fita, estado_atual.nome, qtdPassos)
