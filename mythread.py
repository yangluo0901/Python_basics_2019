import threading
import time

lock = threading.Lock()
num = 100


def run(name):
    lock.acquire()
    global num
    num = num - 1
    print(name, " is runing -------, number is ", num, "\n")
    # time.sleep(5)
    lock.release()


thread_list = []
for n in range(1, 101):
    name = f"thread # {n}"
    thread_list.append(threading.Thread(target=run, args=(name,)))

for element in thread_list:
    element.start()
    element.join()  # wait until the thread terminates, this blocks the calling thread (main thread) until the thread whose join()
                    # method is called terminates


print("Main thead ends ---------------------")
