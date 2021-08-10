#simulador de dados
#simular um uso de um dado o, gerando um valor de 1 até 6
import random
import pySimpleGUI
class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? (s/n)'
        #Layout
        layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'),sg.Button('Não')]
        ]
        #criar uma janela
        self.janela = sg.Window('Simulador de Dado',Layout=layout)
        #ler os valores da tela
        self.eventos, self.valores = janela.Read()
        #fazer alguma coisa com os valores
    
    def Iniciar(self):
        #criar uma janela
        self.janela = sg.Window('Simulador de Dado',Layout=layout)
        #ler os valores da tela
        self.eventos, self.valores = janela.Read()
        #fazer alguma coisa com os valores
        while True:
            try:
                
                if  self.eventos =='s' or  self.eventos == 'sim':
                    self.GerarValorDoDado()
                elif  self.eventos == 'n' or  self.eventos == 'não':
                    print("Tchau!")
                else:
                    print("Favor digitar s para sim ou n para não!")
            except:
                print("Ocorreu um erro!")

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()