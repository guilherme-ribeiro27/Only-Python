#simulador de dados
#simular um uso de um dado o, gerando um valor de 1 até 6
import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? (s/n)'
    
    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 's' or resposta == 'sim':
                self.GerarValorDoDado()
            elif resposta == 'n' or resposta == 'não':
                print("Tchau!")
            else:
                print("Favor digitar s para sim ou n para não!")
        except:
            print("Ocorreu um erro!")

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()