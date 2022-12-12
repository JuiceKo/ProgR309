import threading
import time


class MyProcess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        i = 0
        while i < 3:
            print(i)
            time.sleep(0.4)
            i += 1


thread1 = MyProcess()
thread2 = MyProcess()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("FIN")