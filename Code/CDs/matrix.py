from symbol import Symbol

class Matrix(Symbol):
    '''
    class describing a matrix
    '''
    
    def __init__(self, *rows):
        """
        constructor function for a matrix (list of rows)
        """
        previouslen = len(rows[0].elements)
        for row in rows:
            if previouslen != len(row.elements):
                    raise RowLengthError(previouslen)
            previouslen = len(row.elements)
        self.rows = list(rows)

    def __str__(self):
        """
        function which prints out a matrix
        """
        str_ = ""
        for row in self.rows:
                for element in row.elements:
                        str_ += str(element)
                        str_ += ","
                str_+="\n"
        return str_
    
    @staticmethod
    def name():
        return 'matrix'

    @staticmethod
    def dictionary():
        return 'linalg2'

    @staticmethod
    def put(element):
        """ Matrix element encoding method.
        
        Creates a new OMA element and encodes the matrix to be
        stored within.

        :param element: The matrix object representing the matrix
        :returns: The OMA element representing the given matrix
        """
        omelt = Element("OMA")
        oms = Element("OMS")
        oms.attrib = {'cd' : 'linalg2', 'name' : 'matrix'}
        omelt.insert(1, oms)
        index = 1
        for row in element.rows:
            index += 1
            row_element = MatrixRow.put(row)
            omelt.insert(index, row_element)
        return omelt
    
    def flatten(self):
        """
        Flattens a matrix by retrieving the lists of elements
        from each row
        """
        return [element for row in self.rows for element in row.elements]
        

class MatrixRow(Symbol):
    '''
    class describing a matrix row
    '''

    def __init__(self, *elements):
        """
        instantiates a matrix row with a list of elements
        """
        self.elements = list(elements)

    def __str__(self):
        """
        Prints out a matrix row
        """
        str_ = ""
        for i in self.elements:
                str_+= str(i)
                str_ += ", "
        return str_

    @staticmethod
    def name():
        return 'matrixrow'

    @staticmethod
    def dictionary():
        return 'linalg2'

    @staticmethod
    def put(element):
        """ Matrix row element encoding method.

        Creates a new OMA element and encodes the matrix row to be
        stored within
        
        :param element: The list representing the matrix row
        :returns: The OMA element representing the given matrix row
        """

        omelt = Element("OMA")
        oms = Element("OMS")
        oms.attrib = {'cd' : 'linalg2', 'name' : 'matrixrow'}
        omelt.insert(1, oms)
        index = 1
        for item in element.elements:
            index = index + 1
            omelt.insert(index, om_element(item))
        return omelt


class RowLengthError(Exception):
    '''
    Exception detailing that a matrix has an inconsistency in its rows' length
    '''
    def __init__(self,value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)
    
