from maquina.Maquina import Maquina

class Manager:

    def __init__(self):
        self.Maquina = Maquina()

    def carregar_maquina(self, caminhoDoArquivo, fita):
        self.Maquina.carregamento(caminhoDoArquivo)
        self.Maquina.inserirFita(fita)
        return self.carregou()

    def carregou(self):
        if self.Maquina.existPrograma():
            self.Maquina.startMaquina()
            return True
        else:
            return False
