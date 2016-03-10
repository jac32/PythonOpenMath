import xml.etree.ElementTree as ET

Element = ET.Element
subelement = ET.SubElement


class UnsupportedCDError(Exception):
    def __init__(self, cd, name):
        self.cd = cd
        self.name = name
        self.obj = self.build()

    def __str__(self):
        return ET.tostring(self.obj)

    def build(self):
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
    def __init__(self, cd, name):
        self.cd = cd
        self.name = name
        self.obj = self.build()

    def __str__(self):
        return ET.tostring(self.obj)

    def build(self):
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
    """
    Class describing an error in the OpenMath XML that was passed in originally
    """
    def __str__(self):
        """
        prints out the error message
        """
        return "Cannot divide by Zero"


class InvalidArgsError(Exception):
    """
    Class describing an error in the OpenMath XML that was passed in originally
    """
    def __str__(self):
        """
        prints out the error message
        """            
        return "Too many or too little args"
  
