from threading import Thread
import socket

#Définition envoit et reception
def Envoit(client):
    msg = input()
    msg = msg.encode()
    client.send(msg)


def Reception():
    msg_recu = conn.recv(1024)
    msg_client = msg_recu.decode()
    print(f"Message du client : {msg_client}")


#Port/Host
Host = "localhost"
Port = 8000

while Reception != "kill":
    # Ouverture Socket
    serveur_socket = socket.socket()
    serveur_socket.bind((Host, Port))
    serveur_socket.listen(1)
    print("Attente d'un client")


    while Reception != "reset" and "kill":
        conn, address = serveur_socket.accept()

        print("Le client d'ip", address, "s'est connecté")
        while Reception !="kill" and "disconnect" and "reset":
            envoi = Thread(target=Envoit, args=[conn])
            recep = Thread(target=Reception, args=[conn])
            envoi.start()
            recep.start()

    conn.close()











