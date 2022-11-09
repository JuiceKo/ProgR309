import socket
import sys
def main():

    bye = "bye"
    reply = "j'ai reçu là"
    reply2 = "Le serveur s'éteind"
    port = 18000
    host = "localhost"
    server_socket = socket.socket()
    server_socket.bind((host,port))
    print(f"attente du client sur le port {port} depuis la machine {host}")
    server_socket.listen(1)
    conn, address = server_socket.accept()
    data = conn.recv(1024).decode()
    conn.send(reply.encode())
    print(data)
    data = conn.recv(1024).decode()
    conn.send(reply2.encode())
    if data == "bye":
        conn.close()
        print("Le serveur s'est arrêté")


if __name__ == '__main__':
    sys.exit(main())