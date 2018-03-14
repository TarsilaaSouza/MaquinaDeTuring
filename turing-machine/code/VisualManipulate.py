import time
from Administrator import Manager

class VisualUser:

    def __init__(self):
        self.manager = Manager()

    def start(self):

        self.print_inicio()

        while True:

            TEXTO_INICIAL = "Pressione uma opcao para executar um programa, ou E para sair:"

            option = raw_input(TEXTO_INICIAL)

            if option.lower() == 'i':
                path = self.get_program_path()
                if self.data_validator.validade_path(path):
                    tape = self.get_input_word()
                    self.manager.mount_machine(path, tape)
                else:
                    print ("Wrong program path!!!")

            elif option.lower() == 'e':
                print ("Fechando...")
                time.sleep(0.5)
                break
            else:
                print ("Invalid option")  # to do: exception

    def print_inicio(self):
        instrucoes = "=== Projeto Turing Simulator - Teoria da Computacao 2017.2 ===\n" \
                 "Instrucoes:
                 "
        print instrucoes

    def opcoes(self):
        opcoes = "1 - Palindromo \n" \
                "2 - Adicao de binario \n" \
                "3 - Multiplicacao de binario"
                "4 - Checar parenteses"
                "5 - Expressao boleana em notacao polonesa"
                "6 - Turing Sequence Machine"
                "7 - Universal Turing Machine"
                "8 - Numero Primo em binario"
                "9 - 4 State busy beaver"
                "10 - Binario para decimal"

    def get_program_path(self):
        print ("> Escolha a funcao da maquina e pressione enter:")
        path = raw_input()
        return path

    def get_input_word(self):
        print ("> Write the input word:")
        word = raw_input()
        return word

    def validade_path(path):
        try:
            open(path, "r")
            return True
        except IOError:
            return False
