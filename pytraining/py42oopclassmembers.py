"""
class members

from datetime import datetime
print(datetime.now())
"""


class MaxConnError(Exception):
    """"""


class Connections:
    conn_cntr = 0
    max_conn = 5  # class variable

    def __init__(self, conn_id):
        self.conn_id = conn_id
        Connections.conn_cntr += 1
        Connections.check_limit()

    @classmethod
    def check_limit(cls):
        if cls.conn_cntr > cls.max_conn:
            raise MaxConnError('Max conn limit reached !')


def main():
    conn_list = []
    try:
        for item in range(1, 11):
            conn_list.append(Connections(item))
    except MaxConnError as err:
        print(err)

    for conn in conn_list:
        print(conn)


if __name__ == '__main__':
    main()
