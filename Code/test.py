class Matrix(object):
    '''
    class describing a matrix
    '''
    
    def __init__(self, *rows):
        """
        constructor function for a matrix (list of rows)
        """
        self.rows = rows

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

    def flatten(self):
        """
        Flattens a matrix by retrieving the lists of elements
        from each row
        """
        return [element for row in self.rows for element in row.elements]
        

class MatrixRow(object):
    '''
    class describing a matrix row
    '''

    def __init__(self, *elements):
        """
        instantiates a matrix row with a list of elements
        """
        self.elements = elements

    def __str__(self):
        """
        Prints out a matrix row
        """
        str_ = ""
        for i in self.elements:
                str_+= str(i)
                str_ += ", "
        return str_
    

def oms_linalg2_matrixrow(elements):
    """ Parses a row in a matrix, which consists
        of a list of OpenMath nodes.

    Simply returns the list of elements unaltered.

    :param elements: A list of elements
    :returns: The list of elements
    :rtype: list
    """
    return MatrixRow(*elements)



def oms_linalg2_matrix(rows):
    """ Parses a matrix, which consists of a list of OpenMath matrix rows.

    Simply returns the list of elements unaltered, provided
    all rows are of the same length.

    :param rows: A list of matrix rows
    :returns: The list of rows
    :rtype: list
    """
    previouslen = len(rows[0].elements)
    for row in rows:
            if previouslen != len(row.elements):
                    raise RowLengthError(previouslen)
            previouslen = len(row.elements)
    return Matrix(*rows)


class RowLengthError(Exception):
    '''
    Exception detailing that a matrix has an inconsistency in its rows' length
    '''
    def __init__(self,value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)
    
