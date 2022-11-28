from threading import Thread
import socket


Host = "localhost"
Port = 8000


socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind((Host,Port))

socket.listen(1)


print("Attente d'un client")
client, ip = socket.accept()
print("Le client d'ip",ip,"s'est connecté")


def Envoit(client):
    while True:
        msg = input()
        msg = msg.encode()
        client.send(msg)

def Recoit(client):
    while True:
        msg_client = client.recv(1024)
        msg_client = msg_client.decode()
        print(msg_client)
        if msg_client == "disconnect":
            msg = "le client va être déconnecté"
            msg = msg.encode()
            client.send(msg)
            client.close()




envoi = Thread(target=Envoit,args=[client])
recep = Thread(target=Recoit,args=[client])

envoi.start()
recep.start()

recep.join()

client.close()
socket.close()