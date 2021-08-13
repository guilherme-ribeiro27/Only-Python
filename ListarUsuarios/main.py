import PySimpleGUI as sg
import mysql.connector
sg.theme('BluePurple') 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='pythonusers'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT nome,email FROM usuarios")




def Iniciar(mycursor=mycursor):
    layout = [
        [sg.Text('Usuários')],
        [sg.Text('Nome: ',size=(10,0)), sg.Output(size=(15,1), key='-OUTPUT1-')],
        [sg.Text('Email: ',size=(10,0)), sg.Output(size=(15,1), key='-OUTPUT2-')],
        [sg.Button('Mostrar'),sg.Exit()]
    ]

    janela = sg.Window('Usuários',layout=layout)
    eventos, valores = janela.Read()
    while True:
        if eventos == "Mostrar":            
            janela['-OUTPUT1-'].update('oi')
            continue
        elif eventos == "Exit" or eventos == janela.WIN_CLOSED:
            break
    janela.close()

Iniciar(mycursor)

