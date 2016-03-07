class List(object):
        '''
        class describing an openmath list
        '''

        def __init__(self,elements):
                """
                constructor function for a list instance
                """

                self.elements = elements
                self.oms_list1_list(self.elements)
        
        def __str__(self):
                """
                function describing printing out lists
                """
                str_ = ""
                for i in self.elements:
                        str_+= str(i)
                        str_ += ", "
                return str_
        
        def oms_list1_list(self,elements):
                """ Parses a list of OpenMath nodes.

                Simply returns the list of elements unaltered.

                :param elements: A list of elements
                :returns: The list of elements
                :rtype: list
                """
                return elements


