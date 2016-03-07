'''
Created on 7/3/2016

'''
from _ast import Num
from math import factorial

class Factorial(object):
    '''
    Class describing Factorials in open math
    '''


    def __init__(self, num):
        """
        Constructor for a factorial from open math
        """
        self.num = num
        self.oms_integer1_factorial(num)
        
    def __str__(self):
        """
        Method to print out the factorial which this instance represents
        """
        return str(self.num) + "!" 
    
    def oms_interger1_factorial(self,num):
        """ Parses a matrix, which consists of a list of OpenMath matrix rows.

        Simply returns the list of elements unaltered, provided
        all rows are of the same length.

        :param num: the number to calculate the factorial of
        :returns: The representation of the factorial
        :rtype: int
        """
        return factorial(num)       