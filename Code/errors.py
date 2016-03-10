import xml.etree.ElementTree as ET

Element = ET.Element
subelement = ET.SubElement


class UnsupportedCDError(Exception):
    """Class representing an OpenMath error when a CD is not recognised
    """
    def __init__(self, cd, name):
        """Constructor for an unsupported CD. 
        Takes the CD which raised the exception and the name of the OMS element
        """
        self.cd = cd
        self.name = name
        self.obj = self.build()

    def __str__(self):
        return ET.tostring(self.obj)

    def build(self):
        """The following method constructs an OpenMath OME element representing the unrecognised CD. 
        """
        omobj = Element('OMOBJ')
        ome = Element('OME')

        oms1 = Element('OMS')
        oms1.attrib = {'cd': 'error',
                       'name': 'unsupported_CD'}

        oms2 = Element('OMS')
        oms2.attrib = {'cd': self.cd,
                       'name': self.name}

        omobj.insert(1, ome)
        ome.insert(1, oms1)
        ome.insert(2, oms2)

        return omobj


class UnexpectedSymbolError(Exception):
    """Class representing an OME OpenMath error when a valid CD is accompanied by an unknown name. 
    """
    def __init__(self, cd, name):
        """Constructor for an uunexpected name. 
        It takes the name which raised the exception and the CD of the OMS element
        """
        self.cd = cd
        self.name = name
        self.obj = self.build()

    def __str__(self):
        return ET.tostring(self.obj)

    def build(self):
        """Constructs an OpenMath OME element representing
        the unexpected symbol. 
        """
        omobj = Element('OMOBJ')
        ome = Element('OME')
        oms1 = Element('OMS')

        oms1.attrib = {'cd': 'error',
                       'name': 'unexpected_symbol'}

        oms2 = Element('OMS')
        oms2.attrib = {'cd':  self.cd,
                       'name': self.name}

        omobj.insert(1, ome)
        ome.insert(1, oms1)
        ome.insert(2, oms2)

        return omobj


class DivideByZeroError(Exception):
    """Class describing an error in the OpenMath XML that was passed in originally
    """

    def __init__(self):
        """Constructor for a divide by zero exception. 
        It takes the name which raised the exception and the CD of the OMS element
        """
        self.cd = cd
        self.name = name
        self.obj = self.build()
        

    def __str__(self):
        """Prints out the error message
        """
        return "Cannot divide by Zero"

    def build(self):
        """Constructs an OpenMath OME element representing the unexpected symbol. 
        """
        omobj = Element('OMOBJ')
        ome = Element('OME')
        oms1 = Element('OMS')

        oms1.attrib = {'cd': 'arith_error',
                       'name': 'divide_by_zero'}

        oms2 = Element('OMS')
        oms2.attrib = {'cd':  self.cd,
                       'name': self.name}

        omobj.insert(1, ome)
        ome.insert(1, oms1)
        ome.insert(2, oms2)

        return omobj

class InvalidArgsError(Exception):
    """Class describing an error in the OpenMath XML that was passed in originally
    """
    def __str__(self):
        """Prints out the error message
        """            
        return "Too many or too little args"
  
