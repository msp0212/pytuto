import multiprocessing
from random import randint


def task_set(value):
    """child process function"""
    p_name = multiprocessing.current_process().name
    p_id = multiprocessing.current_process().pid

    print(f'{p_name}:{p_id} received value = {value}')


def main():
    """parent process"""
    parent = multiprocessing.current_process()
    print(parent.name, ':', parent.pid)

    for item in range(0, 5):
        p = multiprocessing.Process(target=task_set, name='p' + str(item), args=(randint(1, 100), ))
        p.start()
    for child in multiprocessing.active_children():
        child.join()  # wait for child


if __name__ == '__main__':
    main()
