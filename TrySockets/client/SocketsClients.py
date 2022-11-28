from threading import Thread
import socket

def Envoit(socket):
    while True:
        msg = input()
        msg = msg.encode()
        socket.send(msg)
        print(msg)



def Recoit(socket):
    while True:
        requete_server = socket.recv(1024)
        requete_server = requete_server.decode("utf-8")
        print(requete_server)
        if requete_server == "le client va être déconnecté":
            print("je me déconnecte")
            socket.close()


Host = "localhost"
Port = 8000


socket = socket.socket()
socket.connect((Host,Port))


envoi = Thread(target=Envoit,args=[socket])
recep = Thread(target=Recoit,args=[socket])

envoi.start()
recep.start()