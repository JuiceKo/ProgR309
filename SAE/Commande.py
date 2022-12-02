import platform
import os
import psutil # télécharger la lib psutil
import socket



while True :
    command = input()
    if command =="OS":
        print(platform.system(),platform.release())
    elif command =="Name":
        print(socket.gethostname())
    elif command == "CPU":
        print('Le CPU est utilisé à :', psutil.cpu_percent(4), '%')
    elif command == "RAM":
        print('Il y a', psutil.virtual_memory()[0] / 1000000000, ' GB de RAM au total,',psutil.virtual_memory()[3] / 1000000000, 'GB de RAM utilisée et',psutil.virtual_memory()[4] / 1000000000, 'GB de RAM libre.' )
    elif command == "IP":
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        print("Votre adresse ip est :", IPAddr)

