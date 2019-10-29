"""
python -m pip install pyexcel pyexcel-xlsx
"""
import logging
import threading
import pyexcel
from time import sleep
from py38assign_sshclient import CustomSSHClient

logging.basicConfig(format='%(threadName)s:%(message)s')
target_file = '__sshresponse.log'


class ThreadSSHClient(CustomSSHClient):
    def __init__(self, host, port, user, pwd, job, lock_obj):
        super().__init__(user, pwd, host, port)
        self.job = job
        self.lock_obj = lock_obj
        self.t_name = threading.current_thread().name
        self.task_runner()

    def task_runner(self):
        payload = self.run_cmd(self.job)
        caption = f'{self.t_name} ran {self.job} @ {self.host}'
        logging.warning('check for the lock')

        with self.lock_obj:
            logging.warning('acquired the lock')
            with open(target_file, 'a') as fw:
                # critical section
                sleep(1)
                fw.write(caption.center(80, '-') + '\n')
                fw.write(payload + '\n')

            logging.warning('release the lock')


def main():
    sheet = pyexcel.get_sheet(file_name=r'D:\Work\pytest\jobs.xlsx')
    lock_obj = threading.Lock()  # sync using lock

    for ssh_host_info in sheet:
        ssh_host_info.append(lock_obj)
        threading.Thread(target=ThreadSSHClient, args=ssh_host_info).start()


if __name__ == '__main__':
    main()
