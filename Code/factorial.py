'''
Created on 7/3/2016
'''
class Factorial(object):
    """
    class describing factorials in open math
    """


    def __init__(self, num):
        """
        Constructor for a Factorial instance
        """
        self.num = num
        
        
    def __str__(self):
        """
        Function for printing out a factorial 
        """    
        return self.num + "!"
    
    
def oms_integer1_factorial(num):
    """ Parses a basic OpenMath factorial node.

    Translates between the OpenMath XML representation
    of an factorial, and a class representing factorials

    :param num: the list containing the number
    :returns: an instance of the Factorial class
    :rtype: Factorial
    """
    return Factorial(num[0])
