import time
import sys
import threading

"""import requests"""
import concurrent.futures
import multiprocessing
import pickle


# ############################
# Tâche en mode processus
def task(k):
    print(f"Task starts for 1 second")
    for i in range(10):
        time.sleep(1)
        print(f"Tâche {k} : loop {i}")
    print(f"Task ends")


# ##############################
# Main process
def mainProcess():
    start = time.perf_counter()

    listProcess = []
    for j in range(100):
        listProcess.append(multiprocessing.Process(target=task, args=[j]))

    for j in range(100):
        listProcess[j].start()

    for j in range(100):
        listProcess[j].join()

    end = time.perf_counter()
    print(f"Main process ended in {round(end - start, 2)} second(s)")


# ##############################
# Main process
def mainThread():
    start = time.perf_counter()

    listProcess = []
    for j in range(100):
        listProcess.append(threading.Thread(target=task, args=[j]))

    for j in range(100):
        listProcess[j].start()

    for j in range(100):
        listProcess[j].join()

    end = time.perf_counter()
    print(f"Main process ended in {round(end - start, 2)} second(s)")


# ################################
if __name__ == '__main__':
    sys.exit(mainThread())
