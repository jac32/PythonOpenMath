""" Encoding objects to OpenMath XML
=====================================

This module provides  a number of functions for encoding "objects"
into OpenMath XML format.

"""

# Encoding Python parser for OpenMath (http://www.openmath.org/)
# See https://docs.python.org/3.4/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET
Element = ET.Element
SubElement = ET.SubElement

################################################################
# 
# OpenMath integer (OMI)
#
def OMInt( x ):
    """ Int element encoding method.
    
    Creates a new OMI element and puts the string representation of
    the int within the node.
    
    :param x: The integer to be represented by the OMI element
    :returns: The OMI element representing the given integer
    """
    omelt = Element("OMI")
    omelt.text = str(x)
    return omelt

################################################################
#
# List (list1.list)
#
def OMList( x ):
    """ List element encoding method.
    
    Creates a new OMA element and encodes the list to be stored within.

    :param x: The list to be encoded within an OMA element.
    :returns: The OMA element representing the given list.

    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = { 'cd' : 'list1', 'name' : 'list' }
    omelt.insert(1,oms)
    n = 1
    for t in x: 
        n = n + 1
        omelt.insert(n, OMelement(t))
    return omelt

def OMBool( x ):
    """ Boolean element encoding method.
    
    Creates a new OMA element and encodes the boolean value
    to be stored within.

    :param x: The list to be encoded within an OMA element.
    :returns: The OMA element representing the given bool.
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    if (x):
        oms.attrib = { 'cd' : 'logic1', 'name': 'true' }
    else:
        oms.attrib = { 'cd' : 'logic1', 'name': 'false' }

    omelt.insert(0,oms)
    return omelt

def OMRational ( x ):
    """

    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = { 'cd' : 'nums1', 'name': 'rational' }
    omelt.insert(1,oms)
    omelt.insert(2, OMelement(x[0]))
    omelt.insert(3, OMelement(x[1]))
    return omelt

def OMComplexCartesian( x ):
    """
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = { 'cd' : 'complex1', 'name': 'complex_cartesian' }
    omelt.insert(1,oms)
    omelt.insert(2,OMelement(int(x.real)))
    omelt.insert(3,OMelement(int(x.imag)))
    return omelt

################################################################
#
# OMelement
#
# Dispatches OpenMath encoding method dependently on the type of x
#
def OMelement( x ):
    """ Runs the correct OpenMath encoding method on a given object.

    Dispatches OpenMath encoding method dependently on the type of 
    the object.

    :params x: The element to be encoded.
    :returns: The OpenMath encoded element 
    
    """
    t = type (x)
    if t == int:
        return OMInt(x)
    elif t == list:
        return OMList(x)
    elif t == bool:
        return OMBool(x)
    elif t == tuple:
        return OMRational(x)
    else:# t == complex:
        return OMComplexCartesian(x)

################################################################
#
# OMobject
#
# Wraps OpenMath encoding for x into OpenMath object
#
def OMobject( x ):
    """ Returns the OpenMath encoding of a given object.

    Creates the OMOBJ element and inserts the appropriate elements within.

    :param x: The object to be converted to its OpenMath XML representation
    :returns: XML tree representation of the OpenMath XML object

    """
    omobj = Element("OMOBJ")
    omobj.insert(1,OMelement(x))
    return omobj

################################################################

