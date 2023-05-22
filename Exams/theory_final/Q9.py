from time import sleep, perf_counter
from threading import Thread

# starting_time = perf_counter()
def f1():
    for i in range(5):
        print(f"f1 - {i}")
        sleep(1)

def f2():
    for i in range(5):
        print(f"f2 - {i}")
        sleep(1)

def f3():
    for i in range(5):
        print(f"f3 - {i}")
        sleep(1)
       
def f4():
    for i in range(5):
        print(f"f4 - {i}")
        sleep(1)

t1 = Thread(target=f1)
t2 = Thread(target=f2)
t3 = Thread(target=f3)
t4 = Thread(target=f4)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

# ending_time = perf_counter()
# print(f'Execution time: {ending_time - starting_time}')

