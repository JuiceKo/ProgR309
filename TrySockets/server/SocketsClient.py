from threading import Thread
import socket

def Send(socket):
    while True:
        msg = input()
        msg = msg.encode('utf-8')
        socket.send(msg)


def Reception(socket):
    while True:
        msgb = conn.recv(1024)  # message en by
        message = msgb.decode()
        print(f"Message du client : {message}")

Host = "localhost"
Port = 10000


socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((Host,Port))

envoi = Thread(target=Send,args=[socket])
recep = Thread(target=Reception,args=[socket])

envoi.start()
recep.start()