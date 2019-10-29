import logging

# set log format, default is loglevel:loggername:logmsg
fmt = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
# set log level to debug, default is at warning
# logging.basicConfig(level=logging.DEBUG, format=fmt, filename='error.log', datefmt="%d-%m-%Y %H:%M")
logging.basicConfig(level=logging.DEBUG, format=fmt, filename='error.log')

logging.debug('debug msg')
logging.info('info msg')
logging.warning('warning msg')
logging.error('error msg')
logging.critical('critical msg')
