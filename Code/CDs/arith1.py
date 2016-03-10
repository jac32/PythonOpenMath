import math
import abc
from symbol import Symbol
from fractions import gcd
import xml.etree.ElementTree as ET
import operator 
from functools import *

Element = ET.Element
SUBELEMENT = ET.SubElement

class Arith1(Symbol):
    def __init__(self,*nums):
        
        self.args = nums 

    def eval(self, op, arguments):
        """
        Function for evaluating times expression
        """
        args = [element if isinstance(element,(int,float,complex)) else element.value for element in arguments] 
        return reduce(op, args)    
     

class Arith1Times(Arith1):
    """
    Class describing an OpenMath times node
    """
    def __init__(self,*nums):
        """
        Constructor for an arith1 times instance
        :param nums: the tuple storing the left and right operands
        """
        super().__init__(nums)
        self.value = super().eval(operator.__mul__,nums)           
 
    def __str__(self):
        """
        Function for printing out a times node
        """
        print(self.a + " * " + self.b)

    @staticmethod
    def name():
        return 'times'
    
    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def put(element):
        return arith1_put(element, Arith1Times)

   
class Arith1Divide(Arith1):
    """
    Class describing an OpenMath divide node
    """
    def __init__(self,*nums):
        """
        Constructor for an arith1 divide instance
        :param nums: the tuple storing the left and right operands
        """
        super().__init__(nums)
        self.value = super().eval(operator.__truediv__,nums)           
         
    def __str__(self):
        """
        Function for printing out a divide node
        """
        print(self.a + " / " + self.b)


    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def name():
        return 'divide'
    
    @staticmethod
    def put(element):
        return arith1_put(element, Arith1Divide)

class Arith1Plus(Arith1):
    """
    Class describing an OpenMath plus node
    """
    def __init__(self,*nums):
        """
        Constructor for an arith1 plus instance
        :param nums: the tuple storing the left and right operands
        """
        super().__init__(nums)
        self.value = super().eval(operator.__add__,nums)           
    
    def __str__(self):
        """
        Function for printing out a plus node
        """
        print(self.a + " + " + self.b)

    @staticmethod
    def name():
        return 'plus'
    
    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def put(element):
        return arith1_put(element, Arith1Plus)

class Arith1Minus(Arith1):
    """
    Class describing an OpenMath minus node
    """
    def __init__(self,*nums):
        """
        Constructor for an arith1 plus instance
        :param nums: the tuple storing the left and right operands
        """
        super().__init__(nums)
        self.value = super().eval(operator.__sub__,nums)           
    
    def __str__(self):
        """
        Function for printing out a plus node
        """
        print(self.a + " - " + self.b)

    @staticmethod
    def name():
        return 'minus'
    
    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def put(element):
        return arith1_put(element, Arith1Minus)

class Arith1Power(Arith1):
    """
    Class describing an OpenMath power node
    """
    def __init__(self,*nums):
        """
        Constructor for an arith1 power instance
        :param nums: the tuple storing the left and right operands
        """
        super().__init__(nums)
        self.value = super().eval(operator.__pow__,nums)           
  
    @staticmethod
    def name():
        return 'power'

    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def put(element):
        return arith1_put(element, Arith1Power)
   
class Arith1Abs(Arith1):
    """
    Class describing an OpenMath abs node
    """
    def __init__(self,*num):
        """
        Constructor for an arith1 abs instance
        :param num: stores an operand
        """
        self.a = num[0]
        self.value = self.eval()

    @staticmethod
    def name():
        return 'abs'

    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def put(element):
        omelt = Element("OMA")
        oms = Element("OMS")
        oms.attrib = {'cd' : 'arith1', 'name': 'abs'}
        omelt.insert(1, oms)
        omelt.insert(2, om_element(element.a))
        return omelt

    
    def eval(self):
        """
        Function for evaluating times expression
        """
        if isinstance(self.a, (int, float, complex)):
            return abs(self.a)
        else: 
            return abs(self.a.value)

class Arith1Root(Arith1):
    """
    Class describing an OpenMath root node
    """
    def __init__(self,*nums):
        """
        Constructor for an arith1 root instance
        :param num: the tuple storing the left and right operands
        """
        if len(nums) != 2: raise InvalidArgsError(len(nums))
        self.args = nums
        self.value = self.eval()
   
    @staticmethod
    def name():
        return 'root'

    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def put(element):
        return arith1_put(element, Arith1Root)
    
    def eval(self):
        """
        Function for evaluating root expression
        """
        args = [element if isinstance(element,(int,float,complex)) else element.value for element in self.args] 
        return reduce(self.iroot, args)    
     
    def iroot(self,k, n):
        """
        Function taken from http://stackoverflow.com/questions/15978781/how-to-find-integer-nth-roots
        to calculate the nth root of the number
        """
        if n == 0:
            raise DivideByZeroError()
        return k ** (1/n)

class Arith1Gcd(Arith1):
    """
    Class describing an OpenMath gcd node
    """
    def __init__(self,*nums):
        """
        Constructor for an arith1 gcd instance
        :param nums: the tuple storing the left and right operands
        """
        super().__init__(nums)
        self.value = super().eval(gcd,nums)           
             
    @staticmethod
    def name():
        return 'gcd'

    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def put(element):
        return arith1_put(element, Arith1Gcd)

class Arith1Lcm(Arith1):
    """
    Class describing an OpenMath lcm node
    """
    def __init__(self,*nums):
        """
        Constructor for an arith1 lcm instance
        :param nums: the tuple storing the left and right operands
        """
        super().__init__(nums)
        self.value = super().eval(self.lcm,nums)           
    
    @staticmethod
    def name():
        return 'lcm'

    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def put(element):
        return arith1_put(element, Arith1Lcm)
    
    def lcm(self,a,b):
        """
        Function for evaluating lcm expression
        """
        return abs(a*b) / gcd(a,b) if a and b else 0
    
class Arith1UnMinus(Arith1):
    """
    Class describing an OpenMath unary minus node
    """
    def __init__(self,*num):
        """
        Constructor for an arith1 unary minus instance
        :param num: stores an operand
        """
        self.a = num[0]    
        self.value = self.eval()

    @staticmethod
    def name():
        return 'unary_minus'

    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def put(element):
        omelt = Element("OMA")
        oms = Element("OMS")
        oms.attrib = {'cd' : 'arith1', 'name': 'unary_minus'}
        omelt.insert(1, oms)
        omelt.insert(2, om_element(element.a))
        return omelt
          
    def eval(self):
        """
        Function for evaluating unary minus expression
        """
        if isinstance(self.a, (int, float, complex)):
            return -(self.a)
        else: 
            return -(self.a.value)
   

class DivideByZeroError(Exception):
    """
    Class describing an error in the OpenMath XML that was passed in originally
    """
    def __str__(self):
        """
        prints out the error message
        """            
        return "Cannot divide by Zero"
 
class InvalidArgsLengthError(Exception):
    """
    Class describing an error in the OpenMath XML that was passed in originally
    """
    def __str__(self):
        """
        prints out the error message
        """            
        return "Too many or too little args"
  
def arith1_put(element, class_):
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : class_.dictionary(), 'name': class_.name()}
    omelt.insert(1, oms)
    omelt.insert(2, om_element(element.a))
    omelt.insert(3, om_element(element.b))
    return omelt
