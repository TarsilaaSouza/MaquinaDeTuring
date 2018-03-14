from Administrator import Manager

class VisualUser:

    def __init__(self):
        self.Manager = Manager()

    def start(self):

        self.print_inicio()

        while True:

            TEXTO_INICIAL = "Pressione uma opcao abaixo para executar um programa, ou E para fechar o simulador:"

            option = raw_input(TEXTO_INICIAL + " ")

            if option.lower() == '1':
                path = "programas\palindrome_detector.in"
                if self.validade_path(path):
                    tape = self.get_input_word()
                    self.Manager.carregar_maquina(path, tape)

            elif option.lower() == 'e':
                print ("Finalizado")
                break
            else:
                print ("Invalid option")

    def print_inicio(self):
        instrucoes = "=== Projeto Turing Simulator - Teoria da Computacao 2017.2 ===\n" \

        print instrucoes

    def opcoes(self):
        opcoes = "1 - Palindromo"
        return opcoes

    def get_program_path(self):
        print ("> Escolha a funcao da maquina e pressione enter:")
        path = raw_input()
        return path

    def get_input_word(self):
        print ("-> Insira a fita na maquina:")
        word = raw_input()
        return word

    def validade_path(self, path):
        try:
            open(path, "r")
            return True
        except IOError:
            return False
