'''
Created on 7/3/2016
'''
################################################################
#
# Basic OpenMath elements
#
from fractions import Fraction

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
