import math
import abc
from symbol import Symbol
from fractions import gcd
import xml.etree.ElementTree as ET

Element = ET.Element
SUBELEMENT = ET.SubElement

class Arith1Times(Symbol):
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

    @staticmethod
    def name():
        return 'times'
    
    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def put(element):
        return arith1_put(element, Arith1Times)


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

class Arith1Divide(Symbol):
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


    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def name():
        return 'divide'
    
    @staticmethod
    def put(element):
        return arith1_put(element, Arith1Divide)

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
    
class Arith1Plus(Symbol):
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

    @staticmethod
    def name():
        return 'plus'
    
    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def put(element):
        return arith1_put(element, Arith1Plus)

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

class Arith1Minus(Symbol):
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

    @staticmethod
    def name():
        return 'minus'
    
    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def put(element):
        return arith1_put(element, Arith1Minus)


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

class Arith1Power(Symbol):
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

    @staticmethod
    def name():
        return 'power'

    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def put(element):
        return arith1_put(element, Arith1Power)
    
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

class Arith1Abs(Symbol):
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

class Arith1Root(Symbol):
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
        print("root (" + self.a + ", " + self.b + ")")
        
    
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
        if isinstance(self.a, (int, float, complex)):
            a= self.a
            if isinstance(self.b, (int,float, complex)):
                b= self.b
            else:
                b= self.b.value
        else:
            a= self.a.value 
        return self.iroot(a,b)

    def iroot(self,k, n):
        """
        Function taken from http://stackoverflow.com/questions/15978781/how-to-find-integer-nth-roots
        to calculate the nth root of the number
        """
        return k ** (1/n)

class Arith1Gcd(Symbol):
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
        
    @staticmethod
    def name():
        return 'gcd'

    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def put(element):
        return arith1_put(element, Arith1Gcd)
       
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

class Arith1Lcm(Symbol):
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
          
    @staticmethod
    def name():
        return 'lcm'

    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def put(element):
        return arith1_put(element, Arith1Lcm)
    
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
    
class Arith1UnMinus(Symbol):
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


    
def arith1_put(element, class_):
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : class_.dictionary(), 'name': class_.name()}
    omelt.insert(1, oms)
    omelt.insert(2, om_element(element.a))
    omelt.insert(3, om_element(element.b))
    return omelt
