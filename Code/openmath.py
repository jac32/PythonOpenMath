""" OpenMath Encode/Decode Library
===================================

This module provides methods for encoding and decoding OpenMath 
"objects" from various sources.

"""

# Python parser for OpenMath (http://www.openmath.org/)
# See https://docs.python.org/3.4/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET
Element = ET.Element
SubElement = ET.SubElement

import omparse
from omparse import *

import omput
from omput import *

################################################################

def ParseOMfile(fname):
    """ Parses OpenMath XML from a file.

    Parses the file contents and calls the decoder on the root 
    of the tree produced.

    :param fname: The path to the file containing the XML data
    :returns: The object represented by the file contents
    """
    tree = ET.parse(fname)
    root = tree.getroot()
    omobj = ParseOMroot(root)
    return omobj

def ParseOMstring(omstring):
    """ Parses OpenMath XML from a string.

    Parses the string contents and calls the decoder on the root 
    of the tree produced.

    :params omstring: The string representation of the XML data.
    :returns: The object represented by the XML from the string.
    """
    root = ET.fromstring(omstring)
    omobj = ParseOMroot(root)
    return omobj

################################################################

def OMstring( x ):
    return ET.tostring( OMobject( x ) ) 

def OMprint( x ):
    ET.dump( OMobject( x ) ) 

################################################################

