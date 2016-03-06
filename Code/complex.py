'''
Created on 6/3/2016

'''

class Complex(object):
    '''
    Class describing a complex number
    '''

    def __init__(self, elements):
        '''
        Constructor for the complex number class
        
        :param elements: the list containing the real and imaginary parts
        '''
        if(len(elements) == 2):
            self.a = elements[0] 
            self.b = elements[1]
            self.oms_complex1_complex_cartesian(self.a,self.b)

    def __str_(self):
        """ Overriden string method for printing complex numbers
        
        """
        return self.a + " " + self.b + "j"

    def oms_complex1_complex_cartesian(self,a,b):
        """ Parses an OpenMath ratio node

        Translates between the OpenMath XML representation of a complex
        cartisian number, and a python complex number.

        :param a: the real part of the complex number
        :param b: the imaginary part of the complex number
        :returns: The complex number represented by the node
        :rtype: complex
        """
        return complex(a, b)
    