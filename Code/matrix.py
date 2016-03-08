class Matrix(object):
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

class RowLengthError(Exception):
    '''
    Exception detailing that a matrix has an inconsistency in its rows' length
    '''
    def __init__(self,value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)
    
