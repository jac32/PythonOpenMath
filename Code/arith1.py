'''
Created on 6/3/2016
'''

class Arith1Times:
    """
    Class describing an OpenMath times node
    """
    def __init__(self,a,b):
        """
        Constructor for an arith1 times instance
        :param a: the left operand
        :param b: the right operand
        """
        self.a = a
        self.b = b
             
    def __str__(self):
        """
        Function for printing out a times node
        """
        print(self.a + " x " + self.b)
            
class Arith1Divide:
    """
    Class describing an OpenMath divide node
    """
    def __init__(self,a,b):
        """
        Constructor for an arith1 divide instance
        :param a: the left operand
        :param b: the right operand
        """
        self.a = a
        self.b = b
             
    def __str__(self):
        """
        Function for printing out a divide node
        """
        print(self.a + " / " + self.b)
    
class Arith1Plus:
    """
    Class describing an OpenMath plus node
    """
    def __init__(self,a,b):
        """
        Constructor for an arith1 plus instance
        :param a: the left operand
        :param b: the right operand
        """
        self.a = a
        self.b = b
             
    def __str__(self):
        """
        Function for printing out a plus node
        """
        print(self.a + " +" + self.b)
   
class Arith1Minus:
    """
    Class describing an OpenMath minus node
    """
    def __init__(self,a,b):
        """
        Constructor for an arith1 minus instance
        :param a: the left operand
        :param b: the right operand
        """
        self.a = a
        self.b = b
             
    def __str__(self):
        """
        Function for printing out a minus node
        """
        print(self.a + " +" + self.b)


def oms_arith1_times(num):
    """ Parses a basic OpenMath arith1 times node.

    Translates between the OpenMath XML representation
    of an Arith1Times, and a class representing Arith1Times

    :param num: the list containing the number
    :returns: an instance of the Arith1Times class
    :rtype: Arith1Times
    """
    return Arith1Times(num[0],num[1])

def oms_arith1_divide(nums):
    """ Parses a basic OpenMath arith1 divide node.

    Translates between the OpenMath XML representation
    of an Arith1Divide, and a class representing Arith1Divide

    :param nums: the list containing the number
    :returns: an instance of the Arith1Divide class
    :rtype: Arith1Divide
    """
    return Arith1Divide(nums[0],nums[1])

def oms_arith1_plus(nums):
    """ Parses a basic OpenMath arith1 plus node.

    Translates between the OpenMath XML representation
    of an Arith1Plus, and a class representing Arith1Plus

    :param nums: the list containing the number
    :returns: an instance of the Arith1Plus class
    :rtype: Arith1Plus
    """
    return Arith1Plus(nums[0],nums[1])

def oms_arith1_minus(nums):
    """ Parses a basic OpenMath arith1 minus node.

    Translates between the OpenMath XML representation
    of an Arith1Minus, and a class representing Arith1Minus

    :param nums: the list containing the number
    :returns: an instance of the Arith1Minus class
    :rtype: Arith1Minus
    """
    return Arith1Minus(nums[0],nums[1])
                    