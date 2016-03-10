from symbol import Symbol
from functools import reduce
from operator import __and__ 
from errors import InvalidArgsError

class Dictionary(Symbol):
    '''
    Class describing custom OpenMath dict1 content dictionary
    '''

    def __init__(self, *pairs):
        '''
        Constructor for creating a new dictionary of key-value pairs
        :param pairs: list of key value pairs
        '''
        x = map(lambda x: isinstance(x, KeyValuePair), pairs)
        if not reduce(__and__, x):
            raise InvalidArgsError
        super().__init__(pairs)
        
    @staticmethod
    def name():
        return 'dict'

    @staticmethod
    def dictionary():
        return 'dict'

class KeyValuePair(Symbol):
    '''
    class describing a key value pair as a member of a dictionary
    '''

    def __init__(self, *pair):
        """
        instantiates a key value pair with a tuple of a key and a value
        :param pair: a tuple of key and value
        """
        if len(pair) != 2:
            raise InvalidArgsError(self)
        super().__init__(pair)

    @staticmethod
    def name():
        return 'key_val'

    @staticmethod
    def dictionary():
        return 'dict1'
