from symbol import Symbol
class Factorial(Symbol):
    """
    class describing factorials in open math
    """

    def __init__(self, num):
        """
        Constructor for a Factorial instance
        """
        self.num = num

    def __str__(self):
        """
        Function for printing out a factorial 
        """    
        return self.num + "!"

    @staticmethod
    def name():
        return 'factorial'

    @staticmethod
    def dictionary():
        return 'integer1'

    @staticmethod
    def put(element):
        """ Factorial encoding method
        
        Creates a new OMS element and encodes the factorial to be 
        stored within
    
        :param factorial: the object storing the number
        :return The OMS element representing the factorial 
        """
        omelt = Element("OMA")
        oms = Element("OMS")
        oms.attrib = {'cd':'integer1', 'name':'factorial'}
        omelt.insert(1, oms)
        omelt.insert(2,om_element(element))
        return omelt
