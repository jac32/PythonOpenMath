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
    """This function sets up the socket with the server
    """
    host = 'localhost'
    port = 54345
    
    socket = create_socket(host,port)
    exit_ = False
    while (not exit_):
        exit_ = prompt(socket)
    socket.close()


def create_socket(host='localhost', port=54345):
    """Creates a socket with the given host name and port
    
    :param host: the host of the server. Defaults to 'localhost' if no argument specified
    :param port: the port to connect to. Defaults to '54345' if no argument specified
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
    """Prompts the user for either a file or an OpenMath xml string to send to the server

    :param s: the socket to be passed into the send_msg function
    :return true or false depending on if the user wishes to quit
    """
    choice = input("Do you want to enter a file or enter manually? (f/m/q)"
                   + " \n> ")
    
    if(choice == 'f'):
        str_ = input("Enter in a file \n>")
        try:
            with open(str_,"r") as file:
                msg = file.read()
                send_msg(msg,s)

        except FileNotFoundError as err:
            log('File not Found')

    elif(choice == 'm'):
        msg = input("Enter in an OpenMath expression "
                    + " \n> ")
        send_msg(msg,s)

    elif(choice == 'q'):
        return True
    else: prompt(s)

        
    return False



def send_msg(message, socket):
    """This function controls sending a message across the socket.
    It could be either the contents of a file, or a message typed in 
    by the user

    :param message: the string to be sent to the socket.
    :param socket: the socket representing the connection with the server
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
