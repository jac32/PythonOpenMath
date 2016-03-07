""" OpenMath Decode Server
===========================

A multithreaded implementation of the OpenMath encoding server.
"""

from socket import *
import threading 
import _thread
import datetime


def log(message):
    """ Simple logging method
    Adds timestamp to output
    :param message: The message to be printed
    """
    now  = datetime.datetime.now()
    print('[%s] - %s' % (now.strftime("%Y-%m-%d %H:%M"), message))
    
def handler(clientsock,addr):
    """ Client socket handler 

    Houses the main loop for interaction with a single client
    """
    while 1:
        data = clientsock.recv(BUFSIZ)
        if not data:
            break
        msg = 'echoed:... ' + str(data, 'UTF-8')
        log(msg)
        clientsock.send(bytes(msg, 'UTF-8'))
    clientsock.close()


############################################################
# Initialiser - Listens for connections and passes sockets
#               to their handlers
#

if __name__=='__main__':
    HOST = 'localhost'
    PORT = 54345
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.bind(ADDR)
    serversock.listen(2)

    while 1:
        log('waiting for connection...')
        clientsock, addr = serversock.accept()
        log('...connected from:' + addr[0] )
        _thread.start_new_thread(handler, (clientsock, addr))
