'''
Created on 6/3/2016
'''
from pyparsing import nums

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
        self.res = eval(self.a, self.b)
             
    def __str__(self):
        """
        Function for printing out a times node
        """
        print(self.a + " * " + self.b)
        
    def eval(self):
        """
        Function for evaluating times expression
        """
        if isinstance(self.a, (int, long, float, complex)):
            if isinstance(self.b, (int, long, float, complex)):
                return (self.a * self.b)
            else:
                return (self.a * eval(source))
        elif isinstance(self.b, (int, long, float, complex)):
            return (eval(self.a ) * self.b)
        else :
            return (eval(self.a) * eval(self.b))
   
            
            
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
        self.res = eval(self.a, self.b)
             
    def __str__(self):
        """
        Function for printing out a divide node
        """
        print(self.a + " / " + self.b)
        
    def eval(self):
        """
        Function for evaluating divide expression
        """
        if isinstance(self.a, (int, long, float, complex)):
            if isinstance(self.b, (int, long, float, complex)):
                return (self.a / self.b)
            else:
                return (self.a / eval(source))
        elif isinstance(self.b, (int, long, float, complex)):
            return (eval(self.a ) / self.b)
        else :
            return (eval(self.a) / eval(self.b))
    
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
        self.res = eval(self.a, self.b)
             
    def __str__(self):
        """
        Function for printing out a plus node
        """
        print(self.a + " + " + self.b)
        
    def eval(self):
        """
        Function for evaluating plus expression
        """
        if isinstance(self.a, (int, long, float, complex)):
            if isinstance(self.b, (int, long, float, complex)):
                return (self.a + self.b)
            else:
                return (self.a + eval(source))
        elif isinstance(self.b, (int, long, float, complex)):
            return (eval(self.a ) + self.b)
        else :
            return (eval(self.a) + eval(self.b))
   
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
        self.res = eval(self.a, self.b)
             
    def __str__(self):
        """
        Function for printing out a minus node
        """
        print(self.a + " - " + self.b)
        
    def eval(self):
        """
        Function for evaluating minus expression
        """
        if isinstance(self.a, (int, long, float, complex)):
            if isinstance(self.b, (int, long, float, complex)):
                return (self.a - self.b)
            else:
                return (self.a - eval(source))
        elif isinstance(self.b, (int, long, float, complex)):
            return (eval(self.a ) - self.b)
        else :
            return (eval(self.a) - eval(self.b))
                 
class Arith1Power:
    """
    Class describing an OpenMath power node
    """
    def __init__(self,*nums):
        """
        Constructor for an arith1 power instance
        :param nums: the tuple storing the left and right operands
        """
        self.a = nums[0]
        self.b = nums[1]
        self.res = eval(self.a, self.b)
             
    def __str__(self):
        """
        Function for printing out a power node
        """
        print(self.a + " ^ " + self.b)
        
    def eval(self):
        """
        Function for evaluating power expression
        """
        if isinstance(self.a, (int, long, float, complex)):
            if isinstance(self.b, (int, long, float, complex)):
                return pow(self.a, self.b)
            else:
                return pow(self.a, eval(source))
        elif isinstance(self.b, (int, long, float, complex)):
            return pow(eval(self.a ), self.b)
        else :
            return pow(eval(self.a), eval(self.b))

class Arith1Abs:
    """
    Class describing an OpenMath abs node
    """
    def __init__(self,*num):
        """
        Constructor for an arith1 abs instance
        :param num: stores an operand
        """
        self.a = nums[0]
        self.res = eval(self.a)
             
    def __str__(self):
        """
        Function for printing out a abs node
        """
        print("|" + self.a + "|")
        
    def eval(self):
        """
        Function for evaluating times expression
        """
        if isinstance(self.a, (int, long, float, complex)):
            return abs(self.a)
        else: 
            return abs(eval(self.a))
                 
class Arith1Root:
    """
    Class describing an OpenMath root node
    """
    def __init__(self,*num):
        """
        Constructor for an arith1 root instance
        :param num: the tuple storing the left and right operands
        """
        self.a = nums[0]
        self.b = nums[1]
        self.res = eval(self.a, self.b)
             
    def __str__(self):
        """
        Function for printing out a abs node
        """
        print("root (" + self.a + ", " + self.b + ")")
        

    def iroot(k, n):
        """
        Function taken from http://stackoverflow.com/questions/15978781/how-to-find-integer-nth-roots
        to calculate the nth root of the number
        """
        u, s = n, n+1
        while u < s:
            s = u
            t = (k-1) * s + n // pow(s, k-1)
            u = t // k
        return s
                 
    def eval(self):
        """
        Function for evaluating root expression
        """
        if isinstance(self.a, (int, long, float, complex)):
            if isinstance(self.b, (int, long, float, complex)):
                return iroot(self.a, self.b)
            else:
                return iroot(self.a, eval(source))
        elif isinstance(self.b, (int, long, float, complex)):
            return iroot(eval(self.a ), self.b)
        else :
            return iroot(eval(self.a), eval(self.b))
                 