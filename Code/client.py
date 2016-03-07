""" OpenMath Request Client
=============================

This module provides an instance of a socket client.
"""

import socket
import datetime
import pickle
from server import log

try:
    # create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
except socket.error as msg:
    log( 'Failed to create socket. Error code: '
         + str(msg[0]) + ', Error message: ' + msg[1])
    sys.exit();

log('Socket created')

host = 'localhost'
port = 54345

try:
    remote_ip = socket.gethostbyname(host)

except socket.gaierror:
    # Could not resolve
    log('Hostname could not be resolved. Exiting')
    sys.exit();

log('IP address of ' + host + ' is ' + remote_ip)

# Connect to remote server
s.connect((remote_ip, port))

log ('Socket connected to ' + host + ' on ip ' + remote_ip)

# Send some data to remote server
message = '<OMOBJ><OMI>42</OMI></OMOBJ>'

try:
    #Set the whole string
    s.sendall(bytes(message, 'UTF-8'))
except socket.error:
    #Send failed
    print('Send failed')
    sys.exit()

print('Message sent successfully')
data = pickle.loads(s.recv(1024))
print(str(data))
    

