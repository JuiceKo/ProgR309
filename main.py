import time
import sys
import threading
import requests
import concurrent.futures

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



    """print("------------------------------------------------------------------------------")

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
        T[i].join()"""

    print("------------------------------------------------------------------------------")

    img_urls = [
        'https://pixabay.com/get/gf1a238e2982a8ca3133ba4a9f7cb4db8438be90b74885e72d16ec7e3f604d00e150c9b00b39a98a59942255bd9de38983077cfaa161d1b104bb404d273bae119b07fb9fbf160f3e1f8215081f04eaca2_1920.jpg’,'
        'https://pixabay.com/get/g00f4426320d22da4e94b9ba518ba83dc19a27e8b185a09f91e663d81ca35de6a1fc2d9a6e129497e8974b69e54642cf2bbd099e312460e15b2cdc82efe9cf1e4366f0774f95472d35180f92762342899_1920.jpg'
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
    print(f"Tasks ended in {round(end - start, 2)} second(s)")

    print("------------------------------------------------------------------------------")

if __name__ == '__main__':
    sys.exit(main())


