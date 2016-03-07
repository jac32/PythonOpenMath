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
        self.oms_interger1_factorial(self.num)
        
        
    def __str__(self):
        """
        Function for printing out a factorial 
        """    
        return self.num + "!"
        
    def oms_interger1_factorial(self,num):
        """ Parses a matrix, which consists of a list of OpenMath matrix rows.
    
        Simply returns the list of elements unaltered, provided
        all rows are of the same length.
    
        :param num: the number to calculate the factorial of
        :returns: The representation of the factorial
        :rtype: int
        """
        return factorial(num) 
