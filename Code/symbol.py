import abc

class Symbol(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self):
        return
    
    @abc.abstractmethod
    def name():
        """ Should return the name of the symbol
        """

    @abc.abstractmethod
    def dictionary():
        """ Should return the name of the symbol's CD
        """

    @abc.abstractmethod
    def put(element):
        """ Should create an element tree XML node representing the OMA
        """
