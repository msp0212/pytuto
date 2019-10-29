"""positional or fixed argument functions"""


def power(x, n=0):  # default arguments
    return x**n


def file_copy(src, dst):
    try:
        """
        fp = open(src)
        fw = open(dst, 'w')
        fw.write(fp.read())
        fp.close()
        fw.close()
        """
        with open(src) as fp, open(dst, 'w') as fw:  # context manager
            fw.write(fp.read())

    except(FileNotFoundError, IOError) as err:
        print(err)

print(power(2, 10))
print(power(2))
file_copy('1datatypes', '_out')