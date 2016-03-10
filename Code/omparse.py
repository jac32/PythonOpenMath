""" Parsing OpenMath Objects
=============================

This module provides a number of functions for decoding "objects"
from the parsed XML tree.

"""
import CDs

from symbol import Symbol
from collections import defaultdict
from fractions import Fraction
from errors import UnsupportedCDError, UnexpectedSymbolError

###############################################################

def omdict_lookup(cd, name):
    """ Looks up OMDICTS for the symbol constructor

    Handles error checking for a OMDICT lookup

    :param cd: The string name of the content dictionary
    :param name: The string name of the symbol
    :returns: The symbol constructor
    """
    
    try:
        dict_ = OMDICTS[cd]
    except:
        raise UnsupportedCDError(cd, name)

    try:
        symbol= dict_[name]
    except:
        raise UnexpectedSymbolError(cd, name)

    return symbol


def parse_om_root(root):
    """ Parses a OpenMath XML tree

    Function should be called on the root element of an OpenMath XML tree.
    Should be the main point of interaction with this module.

    :param root: The root node of the XML tree.
    :returns: The Python representation of the OpenMath object.

    :example:

    >>> import openmath
    import openmath
    >>> from openmath import *
    from openmath import *
    >>> s = '<OMOBJ> <OMI>42</OMI> </OMOBJ>'
    s = '<OMOBJ> <OMI>42</OMI> </OMOBJ>'
    >>> tree = ET.fromstring(s)
    tree = ET.fromstring(s)
    >>> omobj = ParseOMroot(tree)
    omobj = ParseOMroot(tree)
    >>> print(omobj)
    print(omobj)
    42
    """
    try:

        return parse_om_element(root[0])
    except(UnsupportedCDError, UnexpectedSymbolError) as err:
        return err.obj

################################################################
#
# Basic OpenMath elements
#
def parse_om_element(obj):
    """ Appropriately parses a OpenMath XML element

    Uses the `parseOMelementHandler` dictionary to fetch the correct parsing
    function based on the element's XML tag.
    This allows for the type of element to be identified and the subtree to be
    handled correctly.

    :param obj: The node of the tree to be parsed
    :returns: The python representation of the OpenMath XML subtree
    """
    return PARSE_OM_ELEMENT_HANDLER[obj.tag](obj)


def parse_oma(node):
    """ Parses the contents of an OpenMath Application node.

    Fetches the children of the node. The first child is a symbol
    so look up its type in the content dictionary and get the
    application function.
    This function should then be applied to the remaining children
    and the result returned.

    :param node: The XML node representing the OpenMath Application.
    :returns: The result of evaluating the OpenMath Application .
    """
    elts = []
    for child in node.findall("*"):
        elts.append(parse_om_element(child))
    return elts[0](*elts[1:len(elts)])

def parse_oms(node):
    """ Parses a OpenMath Symbol node.

    Looks up the OpenMath content dictionaries for the correct
    function for parsing the adjacent nodes.

    :param node: The XML node representing the OpenMath Symbol.
    :returns: The function to apply to the list of adjacent nodes.
    """

    cd = node.get('cd')
    name = node.get('name')
    return omdict_lookup(cd, name)

def parse_var(node):
    return Variable(node.get('name'))


def parse_omf(node):
    """ Parses a basic OpenMath float node.

    Translates between the OpenMath XML representation
    of an float, i.e. an OMF node, and a Python float.

    :param node: The OMF XML node object.
    :returns: The float value of the node.
    :rtype: float
    """
    return float(node.get('dec'))

def parse_omi(node):
    """ Parses a basic OpenMath integer node.

    Translates between the OpenMath XML representation
    of an integer, i.e. an OMI node, and a Python integer.

    :param node: The OMI XML node object.
    :returns: The integer value of the node.
    :rtype: int
    """
    return int(node.text)

def parse_omstr(node):
    """ Parses a basic OpenMath string node.

    Translates between the OpenMath XML representation
    of an string, i.e. an OMI node, and a Python string.

    :param node: The OMI XML node object.
    :returns: The string value of the node.
    :rtype: string
    """
    return node.text

def oms_list1_list(*elements):
    """ Parses a list of OpenMath nodes.

    Simply returns the list of elements unaltered.

    :param elements: A list of elements
    :returns: The list of elements
    :rtype: list
    """
    return list(elements)


def oms_complex1_complex_cartesian(*elements):
    """ Parses an OpenMath ratio node

    Translates between the OpenMath XML representation of a complex
    cartisian number, and a python complex number.

    :param elements: the list representing the real and imaginary parts
    :returns: The complex number represented by the node
    :rtype: complex
    """
    real = elements[0]
    imag = elements[1]
    return complex(real, imag)

def oms_nums1_rational(*elements):
    """ Parses an OpenMath ratio node.

    Translates between the OpenMath XML representation of a rational
    number, and the tuple representation used within this library.

    :param elements: the numerator and denominator of the rational number
    :returns: A pair representing the ratio
    :rtype: tuple
    """
    numerator = elements[0]
    denominator = elements[1]
    return Fraction(numerator,denominator)

def oms_interval1_integer_interval(*elements):
    """ Parses an OpenMath integer interval node

    Translates between the OpenMath XML representation of an
    integer interval, and a python range object

    :param elements: the list containing the lower and upper limits for the range
    :returns: The range of elements represented by the node
    :rtype: range
    """
    lower = elements[0]
    upper = elements[1]
    return range(lower,upper)

PARSE_OM_ELEMENT_HANDLER = {'OMI' : parse_omi, 'OMS' : parse_oms, 'OMA' : parse_oma, 'OMF': parse_omf, 'OMSTR': parse_omstr, 'OMV': parse_var}


OMDICTS = defaultdict(dict)
# logic1 http://www.openmath.org/cd/logic1.xhtml
OMDICTS['logic1']['true'] = True
OMDICTS['logic1']['false'] = False

# nums1    http://www.openmath.org/cd/nums1.xhtml1
OMDICTS['nums1']['rational'] = oms_nums1_rational

# complex1    http://www.openmath.org/cd/complex1.xhtml
OMDICTS['complex1']['complex_cartesian'] = oms_complex1_complex_cartesian

# interval1   http://www.openmath.org/cd/interval1.xhtml
OMDICTS['interval1']['integer_interval'] = oms_interval1_integer_interval

# list1    http://www.openmath.org/cd/list1.xhtml
OMDICTS['list1']['list'] = oms_list1_list

CDs = Symbol.__subclasses__()

for class_ in CDs:
    print(class_.name())
    OMDICTS[class_.dictionary()][class_.name()] = class_
    for subclass in class_.__subclasses__():
        print(subclass.name())
        OMDICTS[subclass.dictionary()][subclass.name()] = subclass



