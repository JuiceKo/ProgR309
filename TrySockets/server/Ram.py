import socket

host = "localhost" # "", "127.0.0.1
port = 10000

message =""
while message != "kill" and "disconnect":

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    print('le server écoute')

    while message != "kill" and "reset" and "disconnect":

        message = ""
        print('En attente du client')
        conn, address = server_socket.accept()
        print(f'Client connecté {address}')

        while message != "disconnect" and "reset" and "kill" :

            # Réception du message du client
            msgb = conn.recv(1024) # message en by
            message = msgb.decode()
            print(f"Message du client : {message}")

            # J'envoie un message
            reply = input("Saisir un message : ")
            conn.send(reply.encode())
            print(f"Message {reply} envoyé")
        print("le client se deconnecte")
        conn.close()
        server_socket.close()



    # Fermeture
    conn.close()
    print("Fermeture de la socket client")
    conn.close()
    server_socket.close()
    print("Fermeture de la socket serveur")