from btnaval import Partida
from btnaval import Tabuleiro
import winsound
from tkinter import *
from tkinter.ttk import *
import socket, time
import threading
from tkinter .scrolledtext import *
import os
os.system("start /MIN python servidor.py")
a = time.asctime()
#winsound.PlaySound(winsound.Beep(300,3000), winsound.SND_ASYNC)
print("ola")
print(a[2])

winsound.PlaySound('audio.mp3', winsound.SND_FILENAME )
MAX_BYTES = 65535
serverHost = socket.gethostname()
serverPort = 9999
mensagem = [b'Ola, Bem vindo!']
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((serverHost, serverPort))

for linha in mensagem:
    cliente.send(linha)
    #RESPOSTA DO SERVIDOR
    data = cliente.recv(1024)

    print('Cliente recebeu:', data)


a = '1'

jogo = Tabuleiro()
Tabuleiro.__init__(jogo)

Tabuleiro.posicao_disponivel(jogo, 15,15)

print("BEM-VINDO AO JOGO BATALHA NAVAL!\n\nINFORMACOES DO JOGO:\n\nTAMANHO TABULEIRO:",
      str(TAM_PADRAO) + "x" + str(TAM_PADRAO), "\nLETRAS: " + LETRAS_TABULEIRO[0] + "-" + LETRAS_TABULEIRO[
          TAM_PADRAO - 1] + " --> Linhas" + "\nNUMEROS: 1-" + str(TAM_PADRAO) + " --> Colunas")
cliente.close()



