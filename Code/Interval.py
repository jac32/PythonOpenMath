'''
Created on 6/3/2016
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
            self.lower = elements[0]
            self.upper = elements[1]
            self.oms_interval1_integer_interval(self.lower,self.upper)
    
    def __str__(self):
        """
        String method to print out the described range
        """
        return str(self.lower) +" -> "+ str(self.upper)
        
    def oms_interval1_integer_interval(self, lower,upper):
        """ Parses an OpenMath integer interval node

        Translates between the OpenMath XML representation of an
        integer interval, and a python range object

        :param lower: the lower limit for the range
        :param upper: the upper limit for the range
        :returns: The range of elements represented by the node
        :rtype: range
        """
        return range(lower,upper)
