""" Encoding objects to OpenMath XML
=====================================

This module provides  a number of functions for encoding "objects"
into OpenMath XML format.

"""
from fractions import Fraction
from complex import *
from rational import *
from interval import *

# Encoding Python parser for OpenMath (http://www.openmath.org/)
# See https://docs.python.org/3.4/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET
from interval import Interval
Element = ET.Element
SUBELEMENT = ET.SubElement

################################################################
#
# OpenMath integer (OMI)
#
def om_int(int_):
    """ Int element encoding method.

    Creates a new OMI element and puts the string representation of
    the int within the node.

    :param x: The integer to be represented by the OMI element
    :returns: The OMI element representing the given integer
    """
    omelt = Element("OMI")
    omelt.text = str(int_)
    print(omelt.text)
    return omelt

################################################################
#
# OpenMath rational
#
def om_rational(ratio):
    """ Rational number encoding method.

    Creates a new OMA element and encodes the ratio to be
    stored within.

    :param x: The tuple representing the ratio
    :returns: The OMA element representing the ratio
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'nums1', 'name': 'rational'}
    omelt.insert(1, oms)
    omelt.insert(2, om_element(ratio.numerator))
    omelt.insert(3, om_element(ratio.denominator))
    return omelt

################################################################
#
# List (list1.list)
#
def om_list(list_):
    """ List element encoding method

    Creates a new OMA element and encodes the list to be
    stored within.

    :param x: The list to be encoded within an OMA element.
    :returns: The OMA element representing the given list.

    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'list1', 'name' : 'list'}
    omelt.insert(1, oms)
    index = 1
    for item in list_:
        index = index + 1
        omelt.insert(index, om_element(item))
    return omelt

def om_matrix(matrix):
    """ Matrix element encoding method.

    Creates a new OMA element and encodes the matrix to be
    stored within.

    :param x: The 2D List representing the matrix
    :returns: The OMA element representing the given matrix
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'linalg2', 'name' : 'matrix'}
    omelt.insert(1, oms)
    index = 1
    for row in matrix:
        index += 1
        row_element = om_matrix_row(row)
        omelt.insert(index, row_element)
    return omelt


def om_matrix_row(row):
    """ Matrix row element encoding method.

    Creates a new OMA element and encodes the matrix row to be
    stored within

    :param x: The list representing the matrix row
    :returns: The OMA element representing the given matrix row
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'linalg2', 'name' : 'matrixrow'}
    omelt.insert(1, oms)
    index = 1
    for item in row:
        index = index + 1
        omelt.insert(index, om_element(item))
    return omelt

def om_bool(bool_):
    """ Boolean element encoding method.

    Creates a new OMA element and encodes the boolean value
    to be stored within.

    :param x: The list to be encoded within an OMA element.
    :returns: The OMA element representing the given bool.
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    if bool_:
        oms.attrib = {'cd' : 'logic1', 'name': 'true'}
    else:
        oms.attrib = {'cd' : 'logic1', 'name': 'false'}

    omelt.insert(0, oms)
    return omelt



def om_complex_cartesian(complex_num):
    """Complex number encoding method.

    Creates a new OMA element and encodes the complex number to
    be stored within

    :param complex_num: The complex number to be encoded
    :returns: The OMA element representing the complex number
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'complex1', 'name': 'complex_cartesian'}
    omelt.insert(1, oms)
    omelt.insert(2, om_element(complex_num.real))
    omelt.insert(3, om_element(complex_num.imag))
    return omelt

def om_integer_interval(interval):
    """ Integer interval encoding method.

    Creates a new OMA element and encodes the range to be
    stored within.

    :param limits: The inclusive limits for the range (as a list)
    :returns: The OMA element representing the range
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'interval1', 'name': 'integer_interval'}
    omelt.insert(1, oms)
    omelt.insert(2, om_element(interval.lower))
    omelt.insert(3, om_element(interval.upper))
    return omelt
################################################################
#
# om_element
#
def om_element(element):
    """ Runs the correct OpenMath encoding method on a given object.

    Dispatches OpenMath encoding method dependently on the type of
    the object.

    :params element: The element to be encoded.
    :returns: The OpenMath encoded element

BROKEN: isinstance returns false

    """
    if isinstance(element, int):
        return om_int(element)
    elif isinstance(element, Rational):
        return om_rational(element)
    elif isinstance(element, list):
        return om_list_element(element)
    elif isinstance(element, bool):
        return om_bool(element)
    elif isinstance(element, Complex):
        return om_complex_cartesian(element)
    elif isinstance(element, Interval):
        return om_integer_interval(element)


def om_list_element(element):
    """ Produces the correct list element type.

    Multiple OMA elements are represented by lists.
    This function inspects the list to decide which OMA it
    represents.

    :params element: The list representation of the element
    :returns: The OpenMath representation of the element
    """
    if isinstance(element[0], list):
        return om_matrix(element)
    else:
        return om_list(element)


################################################################
#
# OMobject
#
# Wraps OpenMath encoding for x into OpenMath object
#
def om_object(object_):
    """ Returns the OpenMath encoding of a given object.

    Creates the OMOBJ element and inserts the appropriate elementsq
    within.

    :param object_: The object to be converted to its OpenMath XML representation
    :returns: XML tree representation of the OpenMath XML object
    """
    omobj = Element("OMOBJ")
    omobj.insert(1, om_element(object_))
    return omobj

################################################################

