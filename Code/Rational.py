'''
Created on 6/3/2016

'''

class Rational(object):
    '''
    Class describing a rational number
    '''

    def __init__(self, elements):
        '''
        Constructor for the rational number class
        
        :param elements: the list containing the real and imaginary parts
        '''
        if(len(elements) == 2):
            self.numerator = elements[0]
            self.denominator = elements[1]
            self.oms_nums1_rational(self.numerator,self.denominator)
        
    def __str_(self):
        """ Overriden string method for printing rational numbers
        
        """
        return self.numerator + " " + self.denominator + "j"

    def oms_nums1_rational(self,numerator,denominator):
        """ Parses an OpenMath ratio node.

        Translates between the OpenMath XML representation of a rational
        number, and the tuple representation used within this library.

        :param numerator: the numerator of the rational number
        :param denominator: the denominator of the rational number
        :returns: A pair representing the ratio
        :rtype: tuple
        """
        return (numerator,denominator)
