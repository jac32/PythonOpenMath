'''
Created on 6/3/2016
'''

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
        print(self.a + " * " + self.b)
        
    def eval(self):
        """
        Function for evaluating times expression
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
        print(self.a + " / " + self.b)
        
    def eval(self):
        """
        Function for evaluating divide expression
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
        print(self.a + " + " + self.b)
        
    def eval(self):
        """
        Function for evaluating plus expression
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
        print(self.a + " - " + self.b)
        
    def eval(self):
        """
        Function for evaluating minus expression
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
        print(self.a + " ^ " + self.b)
        
    def eval(self):
        """
        Function for evaluating power expression
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
        print("|" + self.a + "|")
        
    def eval(self):
        """
        Function for evaluating times expression
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
        self.res = self.eval()
             
    def __str__(self):
        """
        Function for printing out a abs node
        """
        print("root (" + self.a + ", " + self.b + ")")
        

    def iroot(self,k, n):
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
        if isinstance(self.a, (int, float, complex)):
            a= self.a
            if isinstance(self.b, (int,float, complex)):
                b= self.b
            else:
                b= self.b.value
        else:
            a= self.a.value 
        return self.iroot(a,b)
   
   
def InvalidSyntaxError(Exception):
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