import abc

class Symbol(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self):
        return
    
    @abc.abstractmethod
    def name(self):
        """ Should return the name of the symbol
        """

    @abc.abstractmethod
    def dictionary(self):
        """ Should return the name of the symbol's CD
        """
