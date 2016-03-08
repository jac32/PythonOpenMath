'''
Created on 6/3/2016
'''

class Arith1Times:
    """
    Class describing an OpenMath times node
    """
    def __init__(self,*nums):
        """
        Constructor for an arith1 times instance
        :param nums: the tuple storing the left and right operands
        """
        self.a = nums[0]
        self.b = nums[1]
             
    def __str__(self):
        """
        Function for printing out a times node
        """
        print(self.a + " x " + self.b)
            
class Arith1Divide:
    """
    Class describing an OpenMath divide node
    """
    def __init__(self,*nums):
        """
        Constructor for an arith1 divide instance
        :param nums: the tuple storing the left and right operands
        """
        self.a = nums[0]
        self.b = nums[1]
             
    def __str__(self):
        """
        Function for printing out a divide node
        """
        print(self.a + " / " + self.b)
    
class Arith1Plus:
    """
    Class describing an OpenMath plus node
    """
    def __init__(self,*nums):
        """
        Constructor for an arith1 plus instance
        :param nums: the tuple storing the left and right operands
        """
        self.a = nums[0]
        self.b = nums[1]
             
    def __str__(self):
        """
        Function for printing out a plus node
        """
        print(self.a + " +" + self.b)
   
class Arith1Minus:
    """
    Class describing an OpenMath minus node
    """
    def __init__(self,*nums):
        """
        Constructor for an arith1 minus instance
        :param nums: the tuple storing the left and right operands
        """
        self.a = nums[0]
        self.b = nums[1]
             
    def __str__(self):
        """
        Function for printing out a minus node
        """
        print(self.a + " +" + self.b)
                 