'''
Created on 6/3/2016

@author: Keanan
'''

class Interval(object):
    '''
    Class describing an interval
    '''


    def __init__(self, elements):
        '''
        Constructor for interval class
        :param elements: A list containing the inclusive limits for the range
        '''
        if(len(elements) == 2):
            self.a = elements[0]
            self.b = elements[1]
            #self.oms_interval1_integer_interval(self.a,self.b)
    
    def __str__(self):
        """
        String method to print out the described range
        """
        return str(self.a) +" -> "+ str(self.b)
        
    def oms_interval1_integer_interval(self, elements):
        """ Parses an OpenMath integer interval node

        Translates between the OpenMath XML representation of an
        integer interval, and a python range object

        :param elements: A list containing the inclusive limits for the range
        :returns: The range of elements represented by the node
        :rtype: range
        """
        return range(elements[0],elements[1])
