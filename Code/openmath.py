
""" OpenMath Encode/Decode Library
===================================

This module provides methods for encoding and decoding OpenMath
"objects" from various sources.
"""

# Python parser for OpenMath (http://www.openmath.org/)
# See https://docs.python.org/3.4/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET

from omparse import parse_om_root
from omput import om_object


ELEMENT = ET.Element
SUBELEMENT = ET.SubElement



################################################################

def parse_om_file(fname):
    """ Parses OpenMath XML from a file.

    Parses the file contents and calls the decoder on the root
    of the tree produced.

    :param fname: The path to the file containing the XML data
    :returns: The object represented by the file contents
    """
    tree = ET.parse(fname)
    root = tree.getroot()
    omobj = parse_om_root(root)
    return omobj

def parse_om_string(omstring):
    """ Parses OpenMath XML from a string.

    Parses the string contents and calls the decoder on the root
    of the tree produced.

    :params omstring: The string representation of the XML data.
    :returns: The object represented by the XML from the string.
    """
    root = ET.fromstring(omstring)
    omobj = parse_om_root(root)
    return omobj

def evaluate_om_string(omstring, vars={}):
    """ Evaluates OpenMath XML Strings

    Parses the string contents and calls the evaluator on the 
    root of the tree produced.

    :params omstring: The string representation of the XML data.
    :params vars: A dictionary containing any variables required
    """
    root = ET.fromstring(omstring)
    omobj = parse_om_root(root)
    return omobj.value
 
################################################################

def om_string(object_):
    """ Produces a string representation of an OpenMath XML object

    Creates a string containing the OpenMath XML representation
    of the given object.

    :params x: The object to be encoded to the string
    :returns: The OpenMath XML string representation of the given x
    """
    return ET.tostring(om_object(object_))

def om_print(object_):
    """ Prints the string representation of the object

    Creates a string containing the OpenMath XML representation
    of the given object and outputs it to std out

    :params x: The object to be encoded to the string
    """
    ET.dump(om_object(object_))


def om_pretty_print(node, level=0, indent='\t'):
    """ Pretty prints the string representation of the object
    
    Creates a formatted string containing the OpenMath XML
    representation of the given object and outputs it to 
    std out

    :params x: The object to be encoded to the string
    """
    print('')
    print_indent(level, indent=indent)
    print('<' + node.tag + attrib_string(node) , end='> ')

    children = node.findall('*')
    for child in children:
        om_pretty_print(child, level+1, indent=indent)
    
    if children == []:
        if node.text != None: print(node.text, end=' ')
    elif node.text == None :
        print()
        print_indent(level, indent=indent)
        
    print('</' + node.tag, end='>')


    
def print_indent(level, indent='\t'):
    for i in range(0, level):
        print(indent, end='')

def attrib_string(node):
    str_ = ''
    for attrib in node.attrib:
        str_ = ' '
        str_ += attrib
        str_ += '='
        str_ += node.attrib[attrib]
    return str_
################################################################


