from Arquivo import lerArquivo
from Operacao import Operacao
from Fita import Fita

 #codificao dos simbolos

ESTADO_INICIAL = '0'
ACEITACAO = 'halt-accept'
REJEICAO = 'halt-reject'

class Maquina:

    def __init__(self, Fita=Fita(), Operacao=Operacao()):
        self.Fita = Fitaestados = lerArquivo(caminhoDoArquivo)
        self.Operacao = Operacao

    def existPrograma(self):
        return self.Operacao.existEstado()

    def carregamento(self, caminhoDoArquivo):
        estados = lerArquivo(caminhoDoArquivo)
        self.Operacao.setEstados(estados)

    def inserirFita(self, entrada_fita):
        self.Fita.inserirFita(entrada_fita)

    def print_informacao_atual(self, Fita, estado_atual_nome, qtdPassos):
        print("Estado atual: %s - Posicao: %d - Passos: %d" % (estado_atual_nome, Fita.simbolo_topo, qtdPassos))

    def print_informacao_fita(self, fita):
        print("Fita -> \n" + Fita.simbolo_topo())
        print(fita)

    def verifica_parada(self, nome_ProxEstado, Fita, qtdPassos):

        if nome_ProxEstado == ACEITACAO or nome_ProxEstado == REJEICAO:
            self.print_informacao_atual(self.Fita, nome_ProxEstado, qtdPassos)
            self.print_informacao_fita(self.Fita)
            print("FIM!")
            return True
        elif nome_ProxEstado == "halt":
            self.print_informacao_atual(self.Fita, nome_ProxEstado, qtdPassos)
            self.print_informacao_fita(self.Fita)
            print("FIM!")
            return True
        else:
            return False

    def startMaquina(self):

        qtdPassos = 0
        estado_atual = self.Operacao.proxEstado(ESTADO_INICIAL, self.Fita.simbolo_topo)

        while True:

            if estado_atual is not None:
                self.print_informacao_atual(self.Fita, estado_atual.nome, qtdPassos)
                self.print_informacao_fita(self.Fita)
                qtdPassos += 1
                self.Fita.escrever(estado_atual.novo_simbolo)
                self.Fita.mover(estado_atual.direcao)

                if verifica_parada(estado_atual.proximo_estado, self.Fita, qtdPassos): break

                estado_auxiliar = estado_atual
                estado_atual = self.Operacao.proxEstado(estado_auxiliar.proximo_estado, self.Fita.simbolo_topo)

            else:
                print ("---> FINALIDADO! <---")
                break
