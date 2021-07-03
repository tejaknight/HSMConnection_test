#!/usr/bin/python

import socket
import sys
from sys import exc_info
from traceback import print_exc
import logging
from logging.handlers import TimedRotatingFileHandler



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
t_handler = TimedRotatingFileHandler(filename='connection.log',when='midnight',interval=1)
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
t_handler.setFormatter(f_format)
t_handler.setLevel(logging.DEBUG)


logger.addHandler(t_handler)


ip = ['82.196.241.11','212.64.157.210']
port = 443
retry = 1
delay = 10
timeout = 3

def isOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:        
        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        logger.info(f'ip is up {ip}')
        return True
    except socket.timeout as e:
            print(sys.exc_info())
            logger.error(e.__class__.__name__)
            logger.exception(f'exception when connecting to {ip} ')
            return False
    finally:
        s.close()

    
for i in ip:
    isOpen(i,port)



