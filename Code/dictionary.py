'''
Created on 8/3/2016
'''

class Dictionary(object):
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

        

class KeyValuePair(object):
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
