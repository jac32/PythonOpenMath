'''
Created on 6/3/2016
'''
from math import gcd

class Arith1Times(object):
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
        self.value = self.eval()
             
    def __str__(self):
        """
        Function for printing out a times node
        """
        print(self.a + " * " + self.b + " = " + self.value)
        
    def eval(self):
        """
        Function for evaluating times expression
        :return the instance's 'a' field times its 'b' field
        """
        if isinstance(self.a, (int, float, complex)):
            a= self.a
            if isinstance(self.b, (int,float, complex)):
                b= self.b
            else:
                b= self.b.value
        else:
            a= self.a.value 
        return a * b
            
class Arith1Divide(object):
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
        self.value= self.eval()
             
    def __str__(self):
        """
        Function for printing out a divide node
        """
        print(self.a + " / " + self.b + " = " + self.value)
        
    def eval(self):
        """
        Function for evaluating divide expression
        :return the instance's 'a' field divided by its 'b' field
        """
        if isinstance(self.a, (int, float, complex)):
            a= self.a
            if isinstance(self.b, (int,float, complex)):
                b= self.b
            else:
                b= self.b.value
        else:
            a= self.a.value 
        return a / b
    
class Arith1Plus(object):
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
        self.value = self.eval()
             
    def __str__(self):
        """
        Function for printing out a plus node
        """
        print(self.a + " + " + self.b + " = " + self.value)
        
    def eval(self):
        """
        Function for evaluating plus expression
        :return the instance's 'a' field plus its 'b' field
        """
        if isinstance(self.a, (int, float, complex)):
            a= self.a
            if isinstance(self.b, (int,float, complex)):
                b= self.b
            else:
                b= self.b.value
        else:
            a= self.a.value 
        return a + b

class Arith1Minus(object):
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
        self.value= self.eval()
             
    def __str__(self):
        """
        Function for printing out a minus node
        """
        print(self.a + " - " + self.b + " = " + self.value)
        
    def eval(self):
        """
        Function for evaluating minus expression
        :return the instance's 'a' field minus it's 'b' field
        """
        if isinstance(self.a, (int, float, complex)):
            a= self.a
            if isinstance(self.b, (int,float, complex)):
                b= self.b
            else:
                b= self.b.value
        else:
            a= self.a.value 
        return a - b
                 
class Arith1Power(object):
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
        self.value = self.eval()
             
    def __str__(self):
        """
        Function for printing out a power node
        """
        print(self.a + " ^ " + self.b+ " = " + self.value)
        
    def eval(self):
        """
        Function for evaluating power expression
        :return the instance's 'a' field to the power of its 'b' field
        """
        if isinstance(self.a, (int, float, complex)):
            a= self.a
            if isinstance(self.b, (int,float, complex)):
                b= self.b
            else:
                b= self.b.value
        else:
            a= self.a.value 
        return a ** b

class Arith1Abs(object):
    """
    Class describing an OpenMath abs node
    """
    def __init__(self,*num):
        """
        Constructor for an arith1 abs instance
        :param num: stores an operand
        """
        self.a = num[0]
        self.value= self.eval()
             
    def __str__(self):
        """
        Function for printing out a abs node
        """
        print("|" + self.a + "|" + " = " + self.value)
        
    def eval(self):
        """
        Function for evaluating times expression
        :return the absolute value of the instance's 'a' field
        """
        if isinstance(self.a, (int, float, complex)):
            return abs(self.a)
        else: 
            return abs(self.a.value)
                 
class Arith1Root(object):
    """
    Class describing an OpenMath root node
    """
    def __init__(self,*nums):
        """
        Constructor for an arith1 root instance
        :param num: the tuple storing the left and right operands
        """
        self.a = nums[0]
        self.b = nums[1]
        self.value = self.eval()
             
    def __str__(self):
        """
        Function for printing out a abs node
        """
        print("root (" + self.a + ", " + self.b + ")" + " = " + self.value)
        

    def root(self,base, n):
        """
        Function to calculate the nth root of a number
        :param base: the number being rooted
        :param n: the nth root to be calculated
        :return the nth root of base
        :rtype integer
        """
        return base ** (1/n)
                 
    def eval(self):
        """
        Function for evaluating root expression
        """
        if isinstance(self.a, (int, float, complex)):
            a= self.a
            if isinstance(self.b, (int,float, complex)):
                b= self.b
            else:
                b= self.b.value
        else:
            a= self.a.value 
        return self.root(a,b)

class Arith1Gcd(object):
    """
    Class describing an OpenMath gcd node
    """
    def __init__(self,*nums):
        """
        Constructor for an arith1 gcd instance
        :param nums: the tuple storing the left and right operands
        """
        self.a = nums[0]
        self.b = nums[1]
        self.value = self.eval()
             
    def __str__(self):
        """
        Function for printing out a gcd node
        """
        print("gcd(" + self.a + ", " + self.b + ") = " + self.value)
        
    def eval(self):
        """
        Function for evaluating gcd expression
        """
        if isinstance(self.a, (int, float, complex)):
            a= self.a
            if isinstance(self.b, (int,float, complex)):
                b= self.b
            else:
                b= self.b.value
        else:
            a= self.a.value 
        return gcd(a, b)

class Arith1Lcm(object):
    """
    Class describing an OpenMath lcm node
    """
    def __init__(self,*nums):
        """
        Constructor for an arith1 lcm instance
        :param nums: the tuple storing the left and right operands
        """
        self.a = nums[0]
        self.b = nums[1]
        self.value = self.eval()
             
    def __str__(self):
        """
        Function for printing out a lcm node
        """
        print("lcm(" + self.a + ", " + self.b + ") = " + self.value)
        
    def eval(self):
        """
        Function for evaluating lcm expression
        """
        if isinstance(self.a, (int, float, complex)):
            a= self.a
            if isinstance(self.b, (int,float, complex)):
                b= self.b
            else:
                b= self.b.value
        else:
            a= self.a.value 
        return abs(a*b) / gcd(a,b) if a and b else 0
    
class Arith1UnMinus(object):
    """
    Class describing an OpenMath unary minus node
    """
    def __init__(self,*num):
        """
        Constructor for an arith1 unary minus instance
        :param num: stores an operand
        """
        self.a = num[0]
        self.value= self.eval()
             
    def __str__(self):
        """
        Function for printing out a unary minus node
        """
        print(self.a + " = " + self.value)
        
    def eval(self):
        """
        Function for evaluating unary minus expression
        """
        if isinstance(self.a, (int, float, complex)):
            return -(self.a)
        else: 
            return -(self.a.value)
   
class InvalidSyntaxError(Exception):
    """
    Class describing an error in the OpenMath XML that was passed in originally
    """
    def __init__(self,msg):
        """
        Constructor which instantiates a new instance of this error
        with a message
        :param msg: the message corresponding to the error
        """
        self.msg = msg  
        
    def __str__(self):
        """
        prints out the error message
        """            
        return str(self.msg)