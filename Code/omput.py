""" Encoding objects to OpenMath XML
=====================================

This module provides  a number of functions for encoding "objects"
into OpenMath XML format.

"""
from fractions import Fraction
from matrix import Matrix,MatrixRow
from factorial import Factorial
from arith1 import Arith1Divide, Arith1Minus, Arith1Plus, Arith1Times, Arith1Power, Arith1Abs, Arith1Root
from dictionary import Dictionary,KeyValuePair

# Encoding Python parser for OpenMath (http://www.openmath.org/)
# See https://docs.python.org/3.4/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET
from dictionary import KeyValuePair
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
# OpenMath Factorial
#
def om_factorial(factorial):
    """ Factorial encoding method
    
    Creates a new OMS element and encodes the factorial to be 
    stored within
    
    :param factorial: the object storing the number
    :return The OMS element representing the factorial 
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd':'integer1', 'name':'factorial'}
    omelt.insert(1, oms)
    omelt.insert(2,om_element(factorial))
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
def om_arith1_plus(plus):
    """ Plus arithmetic expression encoding method.

    Creates a new OMA element and encodes the expression to be
    stored within.

    :param plus: The object representing the expression
    :returns: The OMA element representing the expression
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'arith1', 'name': 'plus'}
    omelt.insert(1, oms)
    omelt.insert(2, om_element(plus.a))
    omelt.insert(3, om_element(plus.b))
    return omelt

def om_arith1_minus(minus):
    """ Minus arithmetic expression encoding method.

    Creates a new OMA element and encodes the expression to be
    stored within.

    :param minus: The object representing the expression
    :returns: The OMA element representing the expression
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'arith1', 'name': 'minus'}
    omelt.insert(1, oms)
    omelt.insert(2, om_element(minus.a))
    omelt.insert(3, om_element(minus.b))
    return omelt

def om_arith1_times(times):
    """ Times arithmetic expression encoding method.

    Creates a new OMA element and encodes the expression to be
    stored within.

    :param times: The object representing the expression
    :returns: The OMA element representing the expression
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'arith1', 'name': 'times'}
    omelt.insert(1, oms)
    omelt.insert(2, om_element(times.a))
    omelt.insert(3, om_element(times.b))
    return omelt

def om_arith1_divide(div):
    """ Divide arithmetic expression encoding method.

    Creates a new OMA element and encodes the expression to be
    stored within.

    :param divide: The object representing the expression
    :returns: The OMA element representing the expression
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'arith1', 'name': 'divide'}
    omelt.insert(1, oms)
    omelt.insert(2, om_element(div.a))
    omelt.insert(3, om_element(div.b))
    return omelt

def om_arith1_power(pow_):
    """ Power arithmetic expression encoding method.

    Creates a new OMA element and encodes the expression to be
    stored within.

    :param divide: The object representing the expression
    :returns: The OMA element representing the expression
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'arith1', 'name': 'power'}
    omelt.insert(1, oms)
    omelt.insert(2, om_element(pow_.a))
    omelt.insert(3, om_element(pow_.b))
    return omelt

def om_arith1_abs(abs_):
    """ Abs arithmetic expression encoding method.

    Creates a new OMA element and encodes the expression to be
    stored within.

    :param divide: The object representing the expression
    :returns: The OMA element representing the expression
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'arith1', 'name': 'abs'}
    omelt.insert(1, oms)
    omelt.insert(2, om_element(abs_.a))
    return omelt

def om_arith1_root(root):
    """ Root arithmetic expression encoding method.

    Creates a new OMA element and encodes the expression to be
    stored within.

    :param divide: The object representing the expression
    :returns: The OMA element representing the expression
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'arith1', 'name': 'root'}
    omelt.insert(1, oms)
    omelt.insert(2, om_element(root.a))
    omelt.insert(3, om_element(root.b))
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

def om_dictionary(dictionary):
    """ Dictionary element encoding method.

    Creates a new OMA element and encodes the dictionary to be
    stored within.

    :param dictionary: The dictionary object
    :returns: The OMA element representing the given dictionary
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'dict1', 'name' : 'dict'}
    omelt.insert(1, oms)
    index = 1
    for keyval in dictionary.pairs.iter():
        index += 1
        kv_element = om_key_val(keyval)
        omelt.insert(index, kv_element)
    return omelt

def om_key_val(keyval):
    """ Key Val element encoding method.

    Creates a new OMA element and encodes the key val to be
    stored within

    :param keyval: The keyval Object representing the key val
    :returns: The OMA element representing the given key val pair
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'dict1', 'name' : 'key_val'}
    omelt.insert(1, oms)
    omelt.insert(2, om_element(keyval.key))
    omelt.insert(3, om_element(keyval.value))
    return omelt

def om_matrix(matrix):
    """ Matrix element encoding method.

    Creates a new OMA element and encodes the matrix to be
    stored within.

    :param x: The matrix object representing the matrix
    :returns: The OMA element representing the given matrix
    """
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = {'cd' : 'linalg2', 'name' : 'matrix'}
    omelt.insert(1, oms)
    index = 1
    for row in matrix.rows:
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
    for item in row.elements:
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
# om_arith
#
def om_arith(element):
    """ Runs the correct OpenMath encoding method on a given object.

    Dispatches OpenMath encoding method dependently on the type of
    the object.

    :params element: The element to be encoded.
    :returns: The OpenMath encoded element or None
    """
    if isinstance(element,Arith1Plus):
        return om_arith1_plus(element)
    elif isinstance(element,Arith1Minus):
        return om_arith1_minus(element)
    elif isinstance(element,Arith1Times):
        return om_arith1_times(element)
    elif isinstance(element, Arith1Divide):
        return om_arith1_divide(element)
    elif isinstance(element,Arith1Power):
        return om_arith1_power(element)
    elif isinstance(element,Arith1Abs):
        return om_arith1_abs(element)
    elif isinstance(element,Arith1Root):
        return om_arith1_root(element)
    return None

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
    omelt = om_arith(element)
    if omelt != None:
        return omelt
    elif isinstance(element, int):
        return om_int(element)
    elif isinstance(element,float):
        return om_float(element)
    elif isinstance(element, Factorial):
        return om_factorial(element)
    elif isinstance(element, Dictionary):
        return om_dictionary(element)
    elif isinstance(element, KeyValuePair):
        return om_key_val(element)
    elif isinstance(element, Fraction):
        return om_rational(element)
    elif isinstance(element, list):
        return om_list(element)
    elif isinstance(element, Matrix):
        return om_matrix(element)
    elif isinstance(element,MatrixRow):
        return om_matrix_row(element)
    elif isinstance(element, bool):
        return om_bool(element)
    elif isinstance(element, complex):
        return om_complex_cartesian(element)
    elif isinstance(element, range):
        return om_integer_interval(element)


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

