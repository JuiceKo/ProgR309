import socket





host, port =("127.0.0.1", 5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    socket.connect((host, port))
    print("Client connecté")

    data ="Bonjour je suis le client !"
    data=data.encode("utf8")
    socket.send(data)

except :
    print('Connexion au serveur échoué')
finally:
    socket.close()
