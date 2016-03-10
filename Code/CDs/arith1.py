from abc import abstractproperty
from symbol import Symbol
from fractions import gcd
import xml.etree.ElementTree as ET
import operator
from functools import reduce
from errors import DivideByZeroError, InvalidArgsError

Element = ET.Element
SUBELEMENT = ET.SubElement

class Arith1(Symbol):
    """Super class for the arith1 CD which extends symbol and implements eval
    Has the abstract property op
    to represent the operator that each arith1 class represents
    """
    def __init__(self, nums):
        """Constructor for all things within the arith1 CD. 
        This super constructor instantiates the abstract property 'args' that was
        initially defined within the Symbol super class
        """
        self.args = nums

    @abstractproperty
    def op():
        return

    def eval(self):
        """Method which evaluates the OpenMath arith1 expression that the subclasses represent.
        Uses the corresponding operator and operands specific
        to each instance 
        """
        results = [expr.eval() if isinstance(expr, Symbol)
                 else expr for expr in self.args]

        if len(results) == 1: return self.op()(results[0])
        return reduce(self.op(), results)

class Arith1Times(Arith1):
    """Class describing an OpenMath times node
    """
    def __init__(self, *nums):
        """Constructor for an arith1 times instance
        :param nums: the tuple storing the left and right operands
        """
        super().__init__(nums)

    @staticmethod
    def op():
        return operator.mul

    @staticmethod
    def name():
        return 'times'

    @staticmethod
    def dictionary():
        return 'arith1'


class Arith1Divide(Arith1):
    """Class describing an OpenMath divide node
    """
    def __init__(self, *nums):
        """Constructor for an arith1 divide instance
        :param nums: the tuple storing the left and right operands
        """
        if nums[len(nums)-1] == 0: 
            raise DivideByZeroError()
        super().__init__(nums)

    @staticmethod
    def op():
        return operator.truediv

    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def name():
        return 'divide'


class Arith1Plus(Arith1):
    """Class describing an OpenMath plus node
    """
    def __init__(self, *nums):
        """Constructor for an arith1 plus instance
        :param nums: the tuple storing the left and right operands
        """
        super().__init__(nums)

    @staticmethod
    def op():
        return operator.add

    @staticmethod
    def name():
        return 'plus'

    @staticmethod
    def dictionary():
        return 'arith1'


class Arith1Minus(Arith1):
    """Class describing an OpenMath minus node
    """
    def __init__(self, *nums):
        """Constructor for an arith1 plus instance
        :param nums: the tuple storing the left and right operands
        """
        super().__init__(nums)

    @staticmethod
    def op():
        return operator.sub

    @staticmethod
    def name():
        return 'minus'

    @staticmethod
    def dictionary():
        return 'arith1'

class Arith1Power(Arith1):
    """Class describing an OpenMath power node
    """
    def __init__(self, *nums):
        """Constructor for an arith1 power instance
        :param nums: the tuple storing the left and right operands
        """
        super().__init__(nums)

    @staticmethod
    def op():
        return operator.pow

    @staticmethod
    def name():
        return 'power'

    @staticmethod
    def dictionary():
        return 'arith1'


class Arith1Abs(Arith1):
    """Class describing an OpenMath abs node
    """
    def __init__(self, *num):
        """Constructor for an arith1 abs instance
        :param num: stores an operand
        """

        if len(num) != 1:
            raise InvalidArgsError(self)
        super().__init__(num)

    @staticmethod
    def op():
        return operator.abs

    @staticmethod
    def name():
        return 'abs'

    @staticmethod
    def dictionary():
        return 'arith1'


class Arith1Root(Arith1):
    """Class describing an OpenMath root node
    """

    def __init__(self, *nums):
        """Constructor for an arith1 root instance
        :param num: the tuple storing the left and right operands
        """
        if len(nums) != 2:
            raise InvalidArgsError(self)
        super().__init__(nums)

    @staticmethod
    def name():
        return 'root'

    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def op():
        return Arith1Root.iroot

    @staticmethod
    def iroot(self,k, n):
        if n == 0:
            raise DivideByZeroError()
        return k ** (1/n)


class Arith1Gcd(Arith1):
    """Class describing an OpenMath gcd node
    """
    def __init__(self, *nums):
        """Constructor for an arith1 gcd instance
        :param nums: the tuple storing the left and right operands
        """
        super().__init__(nums)

    @staticmethod
    def op():
        return gcd

    @staticmethod
    def name():
        return 'gcd'

    @staticmethod
    def dictionary():
        return 'arith1'


class Arith1Lcm(Arith1):
    """Class describing an OpenMath lcm node
    """
    def __init__(self,*nums):
        """Constructor for an arith1 lcm instance
        :param nums: the tuple storing the left and right operands
        """
        super().__init__(nums)

    @staticmethod
    def name():
        return 'lcm'

    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def lcm(a, b):
        """Function for evaluating lcm expression
        :param a: the left operand
        :param b: the right operand 
        """
        return abs(a*b) / gcd(a, b) if a and b else 0

    @staticmethod
    def op():
        return Arith1Lcm.lcm

class Arith1UnMinus(Arith1):
    """Class describing an OpenMath unary minus node
    """
    def __init__(self, *num):
        """Constructor for an arith1 unary minus instance
        :param num: stores an operand
        """

        if len(num) != 1:
            raise InvalidArgsError(self)
        super().__init__(num)

    @staticmethod
    def name():
        return 'unary_minus'

    @staticmethod
    def dictionary():
        return 'arith1'

    @staticmethod
    def op():
        return operator.neg

