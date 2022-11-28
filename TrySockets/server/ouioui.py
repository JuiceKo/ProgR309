import socket
from tkinter import *
import tkinter as tkinter
import threading
from tkinter import simpledialog
from tkinter import scrolledtext

HOST = "localhost"
PORT = 7000


class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        msg = tkinter.Tk()
        msg.withdraw()

        self.nickname = simpledialog.askstring('Nickname', "Please choose a Nickname", parent=msg)
        self.gui_done = False

        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg="lightgray")

        self.chat_label = tkinter.Label(self.win, text="chat", bg="lightgray")
        self.chat_label.config(font=("Arial ", 12))
        self.chat_label.pack(padx=20, pady=5)

        self.chat_area = scrolledtext.ScrolledText(self.win)
        self.chat_area.pack(padx=20, pady=5)
        self.chat_area.config(state="disabled")

        self.msg_label = tkinter.Label(self.win, text="Message :", bg="lightgray")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tkinter.Text(self.win, height=3, width=50)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = tkinter.Button(self.win, text="Send", command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True

        self.win.protocol("WM_DELETE_WINDOW", self.stop)

        self.win.mainloop()

    def write(self):
        message = f"{self.nickname}: {self.input_area.get('1.0', 'end')}"
        try:  # on essai l'envoie
            self.sock.send(message.encode('utf-8'))
        except OSError as err:  # si erreur de type OSError
            print("OSError:", err)  # on affiche l'erreur
            recon = self.soc.connect_ex(
                (HOST, PORT))  # on essaie de se reconnecter (on utilise les valeurs globales ici)
            if recon == 0:  # si connexion réussi
                print("reconnecté")  # on l'affiche dans la console
            else:  # sinon on affiche le numéro de l'erreur
                print("échec: erreur", recon)
        else:  # si l'envoi à réussi, on efface l'input_area
            self.input_area.delete('1.0', 'end')

    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)

    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.sock.send(self.nickname.encode('utf-8'))
                else:
                    if self.gui_done:
                        self.chat_area.config(state='normal')
                        self.chat_area.insert('end', message)
                        self.chat_area.yview('end')
                        self.chat_area.config(state='disabled')
            except ConnectionAbortedError:
                break
            except:
                print('Error')
                self.sock.close()
                break


client = Client(HOST, PORT)