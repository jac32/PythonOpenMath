from symbol import Symbol

class Dictionary(Symbol):
    '''
    Class describing custom OpenMath dict1 content dictionary
    '''

    def __init__(self, *pairs):
        '''
        Constructor for creating a new dictionary of key-value pairs
        :param pairs: list of key value pairs
        '''
        self.pairs = dict()
        for obj in pairs:
            self.pairs[obj.key]= obj.value

    def __str__(self):
        """
        function which prints out a dictionary
        """
        str_ = ""
        for pair in self.pairs:
            str_ += str(pair.key) + ": " + str(pair.value)
            str_+="\n"
        return str_

    @staticmethod
    def name():
        return 'dict'

    @staticmethod
    def dictionary():
        return 'dict'

    @staticmethod
    def put(element):
        """ Dictionary element encoding method.

        Creates a new OMA element and encodes the dictionary to be
        stored within.

        :param dictionary: The dictionary object
        :returns: The OMA element representing the given dictionary
        """
        omelt = Element("OMA")
        oms = Element("OMS")
        oms.attrib = {'cd' : 'dict1', 'name' : 'dict'}
        omelt.insert(1, oms)
        index = 1
        for keyval in element.pairs.iter():
            index += 1
            kv_element = KeyValuePair.put(keyval)
            omelt.insert(index, kv_element)
        return omelt

class KeyValuePair(Symbol):
    '''
    class describing a key value pair as a member of a dictionary
    '''

    def __init__(self, *pair):
        """
        instantiates a key value pair with a tuple of a key and a value
        :param pair: a tuple of key and value
        """
        self.key= pair[0]
        self.value = pair[1]

    def __str__(self):
        """
        Prints out a key value pair
        """
        return str(self.key) + ": " + str(self.value)

    @staticmethod
    def name():
        return 'key_val'

    @staticmethod
    def dictionary():
        return 'dict1'

    @staticmethod
    def put(element):
        """ Matrix row element encoding method.

        Creates a new OMA element and encodes the matrix row to be
        stored within

        :param x: The list representing the matrix row
        :returns: The OMA element representing the given matrix row
        """
        omelt = Element("OMA")
        oms = Element("OMS")
        oms.attrib = {'cd' : 'dict1', 'name' : 'key_val'}
        omelt.insert(1, oms)
        omelt.insert(2, om_element(element.key))
        omelt.insert(3, om_element(element.value))
        return omelt
