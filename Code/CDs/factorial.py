from symbol import Symbol
from functools import reduce

class Factorial(Symbol):
    """Class describing factorials in open math
    """

    def __init__(self, *num):
        """Constructor for a Factorial instance
        """
        self.args = num

    @staticmethod
    def name():
        return 'factorial'

    @staticmethod
    def dictionary():
        return 'integer1'

    def eval():
        """Implementation of eval() for Factorials
        The function takes the arg for the instance of the factorial class,
        and reduces the sequence produced by range down to a single number
        """
        return reduce(operator.__mul__, range(1,self.args[0]+1))

