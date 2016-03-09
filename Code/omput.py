""" Encoding objects to OpenMath XML
=====================================

This module provides  a number of functions for encoding "objects"
into OpenMath XML format.

"""

import CDs
from CDs import * 
from symbol import Symbol
from fractions import Fraction

# Encoding Python parser for OpenMath (http://www.openmath.org/)
# See https://docs.python.org/3.4/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET

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

    :param int_: The integer to be represented by the OMI element
    :returns: The OMI element representing the given integer
    """
    omelt = Element("OMI")
    omelt.text = str(int_)
    print(omelt.text)
    return omelt


#################################################################
#
# OpenMath string (OMSTR)
#
def om_str(str_):
    """ Str element encoding method.

    Creates a new OMSTR element and puts the string representation of
    the str within the node.

    :param str_: The integer to be represented by the OMSTR element
    :returns: The OMSTR element representing the given integer
    """
    omelt = Element("OMSTR")
    omelt.text = str_
    print(omelt.text)
    return omelt


################################################################
#
# OpenMath float (OMF)
#
def om_float(float_):
    """ Float element encoding method.

    Creates a new OMF element and puts the string representation of
    the float within the node.

    :param float_: The float to be represented by the OMF element
    :returns: The OMF element representing the given float
    """
    omelt = Element("OMF")
    omelt.attrib = { 'dec' : str(float_)}
    print(omelt.get('dec'))
    return omelt


################################################################
#
# OpenMath rational
#
def om_rational(ratio):
    """ Rational number encoding method.

    Creates a new OMA element and encodes the ratio to be
    stored within.

    :param ratio: The object representing the ratio
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
# Arith (Arith1)
#

def om_arith1_gcd(gcd):
    """ Gcd arithmetic expression encoding method.

    Creates a new OMA element and encodes the expression to be
    stored within.

    :param divide: The object representing the expression
    :returns: The OMA element representing the expression
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'arith1', 'name': 'gcd'}
    omelt.insert(1, oms)
    omelt.insert(2, om_element(gcd.a))
    omelt.insert(3, om_element(gcd.b))
    return omelt

def om_arith1_lcm(lcm):
    """ Lcm arithmetic expression encoding method.

    Creates a new OMA element and encodes the expression to be
    stored within.

    :param divide: The object representing the expression
    :returns: The OMA element representing the expression
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'arith1', 'name': 'lcm'}
    omelt.insert(1, oms)
    omelt.insert(2, om_element(lcm.a))
    omelt.insert(3, om_element(lcm.b))
    return omelt

def om_arith1_unary_minus(un_minus):
    """ Unary minus arithmetic expression encoding method.

    Creates a new OMA element and encodes the expression to be
    stored within.

    :param divide: The object representing the expression
    :returns: The OMA element representing the expression
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'arith1', 'name': 'unary_minus'}
    omelt.insert(1, oms)
    omelt.insert(2, om_element(un_minus.a))
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
    omelt.insert(2, om_element(interval[0]))
    omelt.insert(3, om_element(interval[-1]+1))
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
    """
    if isinstance(element, int):
        return om_int(element)
    elif isinstance(element,float):
        return om_float(element)
    elif isinstance(element, Fraction):
        return om_rational(element)
    elif isinstance(element, list):
        return om_list(element)
    elif isinstance(element, bool):
        return om_bool(element)
    elif isinstance(element, complex):
        return om_complex_cartesian(element)
    elif isinstance(element, range):
        return om_integer_interval(element)

    for class_ in Symbol.__subclasses__():
        if isinstance(element, class_):
            return class_.put(element)

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

