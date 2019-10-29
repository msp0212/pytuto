"""variable number of arguments to functions"""


def demo(*args):
    print(args)


def compute(a, b, c):
    print(a + b + c)

demo()
demo(123)
demo(1, 2, 'test', 4.4, 5+6j)
# pass a list as an argument
items = [1, 2, 3]
demo(items)
# pass contents of list as arguments
demo(*items)
# pass a tuple as an argument
items = (1, 2, 3)
demo(items)
# pass contents of tuple as arguments
demo(*items)

items = [1, 2, 3]
compute(*items)
