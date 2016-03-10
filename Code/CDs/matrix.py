from symbol import Symbol

class Matrix(Symbol):
    '''
    class describing a matrix
    '''
    
    def __init__(self, *rows):
        """
        constructor function for a matrix (list of rows)
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
        """
        Flattens a matrix by retrieving the lists of elements
        from each row
        """
        return [element for row in self.args for element in row.args]
        

class MatrixRow(Symbol):
    '''
    class describing a matrix row
    '''

    def __init__(self, *elements):
        """
        instantiates a matrix row with a list of elements
        """
        self.args = elements

    @staticmethod
    def name():
        return 'matrixrow'

    @staticmethod
    def dictionary():
        return 'linalg2'



class RowLengthError(Exception):
    '''
    Exception detailing that a matrix has an inconsistency in its rows' length
    '''
    def __init__(self,value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)
    
