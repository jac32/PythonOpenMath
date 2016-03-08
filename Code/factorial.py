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
    