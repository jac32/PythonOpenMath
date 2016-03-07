class Matrix(object):
        '''
        class describing a matrix
        '''
        
        def __init__(self,rows):
                """
                constructor function for a matrix (list of rows)
                """
                self.rows = rows
                self.oms_linalg2_matrix(rows)

        def __str__(self):
                """
                function which prints out a matrix
                """
                for i in self.rows:
                        print(i)

        def oms_linalg2_matrix(self,rows):
                """ Parses a matrix, which consists
                    of a list of OpenMath matrix rows.

                Simply returns the list of elements unaltered.

                :param elements: A list of matrix rows
                :returns: The list of rows
                :rtype: list
                """
                return rows


class MatrixRow(object):
        '''
        class describing a matrix row
        '''

        def __init__(self,elements):
                """
                instantiates a matrix row with a list of elements
                """
                self.elements = elements
                self.oms_linalg2_matrixrow(elements)

        def __str__(self):
                """
                Prints out a matrix row
                """
                print(self.elements)

        def oms_linalg2_matrixrow(self,elements):
                """ Parses a row in a matrix, which consists
                    of a list of OpenMath nodes.

                Simply returns the list of elements unaltered.

                :param elements: A list of elements
                :returns: The list of elements
                :rtype: list
                """
                return elements

