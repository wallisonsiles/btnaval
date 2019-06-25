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
winsound.PlaySound(winsound.Beep(300,3000), winsound.SND_ASYNC)
print("ola")
time.sleep(2)
print(a[2])

winsound.PlaySound('audio.mp3', winsound.SND_FILENAME )
MAX_BYTES = 65535
host = 'localhost'
port = 9999
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((host,port))
def receber():
    while True:
        msg = cliente.recv(MAX_BYTES)
        chat.configure(state="normal")
        chat.insert(END, msg)
        chat.see(END)
        chat.configure(state="disabled")

def enviar(event):
        chat.configure(state="normal")
        cliente.send(str(nome + ": " + msg.get()+"\n").encode('utf-8'))
        chat.insert(END, str(nome+": "+msg.get()+"\n"))
        msg.delete(0, END)
        chat.see(END)
        chat.configure(state="disabled")


nome = input("Digite seu nome: ")
janela = Tk()
janela.geometry("300x200")
janela.title(("Bate-papo"))

chat = ScrolledText(janela, height=100, width=80)
chat.pack()
chat.configure(state="normal")
chat.insert(END, "Bem vindo ao chat, {}!\n".format(nome))
chat.configure(state="disabled")
msg = Entry(janela, width=100)
msg.pack()

thread = threading.Thread(target=receber)
thread.start()
msg.bind("<Return>", enviar)

janela.mainloop()
