import platform
import os

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Importing the library
import psutil

# Calling psutil.cpu_precent() for 4 seconds
print('The CPU usage is: ', psutil.cpu_percent(4))

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
while True :
    command = input()
    if command =="OS":
        print(platform.system(),platform.release())
    elif command =="Version":
        print(platform.win32_edition())
    elif command == "Machine":
        print(platform.machine())
    elif command == "Node":
        print(platform.node())
    elif command == "Processor":
        print(platform.processor())
