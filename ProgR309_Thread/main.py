import time
import sys
import threading
"""import requests"""
import concurrent.futures
import multiprocessing

def main():

    print("------------------------------------------------------------------------------")

    def task(i):
        print(f"Task {i} starts")
        time.sleep(1)
        print(f"Task {i} ends")

    start = time.perf_counter()
    task(1)
    end = time.perf_counter()
    print(f"Tasks ended in {round(end-start, 2)} second(s)")

    print("------------------------------------------------------------------------------")


    def task(i):
        print(f"Task {i} starts")
        time.sleep(1)
        print(f"Task {i} ends")

    start = time.perf_counter()
    task(1)
    task(2)
    end = time.perf_counter()
    print(f"Tasks ended in {round(end-start, 2)} second(s)")


    print("------------------------------------------------------------------------------")

    def task(i):
        print(f"Task {i} starts")
        time.sleep(1)
        print(f"Task {i} ends")

    start = time.perf_counter()
    t1 = threading.Thread(target=task, args=[1])  # création de la thread
    t1.start()  # je démarre la thread
    t1.join()  # j'attends la fin de la thread
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")

    print("------------------------------------------------------------------------------")

    start = time.perf_counter()
    t1 = threading.Thread(target=task, args=[1])
    t1.start()
    t2 = threading.Thread(target=task, args=[2])
    t2.start()
    t1.join()  # j'attends la fin de la thread
    t2.join()  # j'attends la fin de la thread
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")

    print("------------------------------------------------------------------------------")

    T = []
    for i in range(100):
        T.append(threading.Thread(target=task, args=[i]))
    for i in range(len(T)):
        T[i].start()
    for i in range(len(T)):
        T[i].join()

    print("------------------------------------------------------------------------------")

    def task(i):
        print(f"Task {i} starts for {i+1} second(s)")
        time.sleep(i+1)
        print(f"Task {i} ends")
        T = []
        for i in range(100):
            T.append(threading.Thread(target=task, args=[i]))
        for i in range(len(T)):
            T[i].start()
        for i in range(len(T)):
            T[i].join()



    print("------------------------------------------------------------------------------")

    def task(i):
        print(f"Task {i} starts for {i + 1} second(s)")
        time.sleep(i + 1)
        print(f"Task {i} ends")

    T = []

    for i in range(100):
        T.append(threading.Thread(target=task, args=[i]))
    for i in range(len(T)):
        T[i].start()
    for i in range(len(T)):
        T[i].join()

    print("------------------------------------------------------------------------------")

    """img_urls = [
        'https://th.bing.com/th/id/OIP.xCJSeJFRUsF2ZAf2ETpQiwHaEK?pid=ImgDet&rs=1'
    ]

    def download_image(img_url):
        img_bytes = requests.get(img_url).content
        img_name = img_url.split('/')[4]
        with open(img_name, 'wb') as img_file:
            img_file.write(img_bytes)
            print(f"{img_name} was downloaded")

    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)

    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")"""

    print("------------------------------------------------------------------------------")

    start = time.perf_counter()
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    end = time.perf_counter()
    print(f"Main Tasks ended in {round(end - start, 2)} second(s)")



if __name__ == '__main__':
    sys.exit(main())


