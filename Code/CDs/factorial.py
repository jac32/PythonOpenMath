from symbol import Symbol
from functools import reduce

class Factorial(Symbol):
    """
    class describing factorials in open math
    """

    def __init__(self, *num):
        """
        Constructor for a Factorial instance
        """
        self.args = num

    @staticmethod
    def name():
        return 'factorial'

    @staticmethod
    def dictionary():
        return 'integer1'

    def eval():
        return reduce(operator.__mul__, range(1,self.args+1))

