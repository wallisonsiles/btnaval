from socket import *
import threading
#DADOS DE CONEXÃO COM O SERVIDOR
host = gethostname()
port = 9999
servidorobj = socket(AF_INET, SOCK_STREAM) #VOCÊ ESTÁ USANDO UM SERVIDOR TCP-IP
servidorobj.bind((host, port))
print("servidor conectado por {}:{}".format(host,port))
servidorobj.listen(5)
'''
def ReceberMensagens(c1, c2):
    while True:
        msg = c1.recv(9999)
        c2.send(msg)

a, b = servidorobj.accept()
print(b)
a2, b2 = servidorobj.accept()
print(b2)
p = threading.Thread(target=ReceberMensagens,args=(a2,a))
p2 = threading.Thread(target=ReceberMensagens,args=(a,a2))
p.start()
p2.start()
'''

while True:
    conexão, endereço = servidorobj.accept() #PASSA OS PARÂMETROS DA CONEXÃO(LOCALHOST) E A PORTA
    print('O servidor está conectado por', endereço)
    while True:
        data = conexão.recv(1024) # O SOCKET VAI ESTAR CONECTADO E RECEBENDO 1024 BYTES DE CONEXÃO
        if not data:
            break
        conexão.send(b'Eco=>' + data )
        
    conexão.close()
