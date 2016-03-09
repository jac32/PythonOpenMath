def Variable(object):
    """
    Class describing an OpenMath variable
    """
    def __init__(self,node):
        """
        Constructor which sets up a new variable
        """
        self.name = node.get('name')

    def __str__(self):
        """
        Function for printing out the variable 
        """
        return self.name

