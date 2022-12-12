import socket
import threading

class ThreadForCLient(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self):
        data = self.conn.recv(1024)
        data.decode('utf8')
        print(data)


host, port=("", 5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("Le serveur est démarré...")

while True:
    socket.listen()
    conn, address = socket.accept()
    print("Un client s'est connecté...")

    my_thread = ThreadForCLient(conn)
    my_thread.start()

conn.close()
socket.close()
