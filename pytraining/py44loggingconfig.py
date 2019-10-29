import logging
from logging.handlers import RotatingFileHandler

fmt_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
fmt = logging.Formatter(fmt_str)  # what to log

handler = RotatingFileHandler('ns.log', maxBytes=32, backupCount=5)  # where to log
handler.setFormatter(fmt)

logger = logging.getLogger('NSLogger')  # user defined logger instance, default is root
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)  # add handler to the logger


if __name__ == '__main__':
    """put logger testing code here"""
