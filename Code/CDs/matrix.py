from symbol import Symbol

class Matrix(Symbol):
    """Class describing an OpenMath matrix
    """
    
    def __init__(self, *rows):
        """Constructor function for a matrix (list of matrix rows)
        The length of the args in each matrix row are analysed and checked
        for consistency. If one row does not match, an exception is raised
        """
        prev = len(rows[0].args)
        for current in map(lambda x: len(x.args), rows):
            if prev != current: raise RowLengthError(current)
            prev = current

        self.args = rows

    @staticmethod
    def name():
        return 'matrix' 

    @staticmethod
    def dictionary():
        return 'linalg2'

   
    def flatten(self):
        """Flattens a matrix into a list
        Does this using a list comprehension. The lists of elements are retreived 
        from each row
        """
        return [element for row in self.args for element in row.args]
        

class MatrixRow(Symbol):
    """Class describing an OpenMath matrix row
    """

    def __init__(self, *elements):
        """Instantiates a matrix row with a tuple of elements
        """
        self.args = elements

    @staticmethod
    def name():
        return 'matrixrow'

    @staticmethod
    def dictionary():
        return 'linalg2'



class RowLengthError(Exception):
    """Exception detailing that a matrix has an inconsistency in its rows' length
    """
    def __init__(self,value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)
    
