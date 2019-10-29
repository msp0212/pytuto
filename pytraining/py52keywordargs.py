"""
keyword arguments in function definition
"""


def tuner(**kwargs):
    print(kwargs)


tuner()
tuner(brightness=1.1)
tuner(contrast=.8, brightness=1.1, hue=2.2)
