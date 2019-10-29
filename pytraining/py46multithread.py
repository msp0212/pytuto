import threading
from time import sleep
from random import random

def worker(delay):
    """thread function"""
    t_name = threading.current_thread().name
    t_id = threading.current_thread().ident
    print(f'{t_name} : {t_id} waited for {delay}')


def main():
    """main thread"""
    for item in range(1, 10):
        rand_val = random()
        t = threading.Thread(target=worker, args=(rand_val, ), name='t' + str(item))
        t.start()

    print(f'{threading.current_thread().name} is terminating...')


if __name__ == '__main__':
    main()
