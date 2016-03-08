""" OpenMath Request Client
=============================

This module provides an instance of a socket client.
"""

import socket
import datetime
import pickle
import sys
from server import log

def setup():
    """
    This function sets up the socket with the server
    """
    host = 'localhost'
    port = 54345
    
    socket = create_socket(host,port)
    prompt(socket)
    socket.close()


def create_socket(host='localhost', port=54345):
    """
    Creates a socket with the given host name and port
    """
    try:
        # create an AF_INET, STREAM socket (TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    except socket.error as msg:
        log( 'Failed to create socket. Error code: '
             + str(msg[0]) + ', Error message: ' + msg[1])
        sys.exit();
    
    log('Socket created')
       
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
    return s    

def prompt(s):        
    """
    This function prompts the user for either a file or an OpenMath xml string
    to send to the server
    """
    choice = input("Do you want to enter a file or enter manually? (y/n)")
    if(choice == 'y'):
        str_ = input("Enter in a file")
        file = open(str_,"r")
        msg = file.read()
        send_msg(msg,s)
        file.close()
    elif(choice == 'n'):
        msg = input("Enter in an OpenMath expression")
        send_msg(msg,s)



def send_msg(message, socket):
    """
    This function controls sending a message across the socket
    """    
    try:
        #Set the whole string
        socket.sendall(bytes(message, 'UTF-8'))
    except socket.error:
        #Send failed
        print('Send failed')
        sys.exit()
    
    print('Message sent successfully')
    data = pickle.loads(socket.recv(1024))
    print(str(data))
        

setup()
