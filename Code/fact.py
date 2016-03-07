'''
Created on 7/3/2016
'''
from math import factorial

class Factorial(object):
    """
    class describing factorials in open math
    """


    def __init__(self, num):
        """
        Constructor for a Factorial instance
        """
        self.num = num[0]
        
    def __str__(self):
        """
        Function for printing out a factorial 
        """    
        return self.num + "!"

