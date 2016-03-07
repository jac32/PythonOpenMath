""" Parsing OpenMath Objects
=============================

This module provides a number of functions for decoding "objects"
from the parsed XML tree.

"""
from Matrix import Matrix,MatrixRow
from applications import *
from fact import *

################################################################
#
# OpenMath content dictionaries
#
OMDICTS = {}

# logic1	http://www.openmath.org/cd/logic1.xhtml
OMDICTS['logic1'] = {}
OMDICTS['logic1']['true'] = True
OMDICTS['logic1']['false'] = False

# nums1    http://www.openmath.org/cd/nums1.xhtml1
OMDICTS['nums1'] = {}
OMDICTS['nums1']['rational'] = oms_nums1_rational

# complex1    http://www.openmath.org/cd/complex1.xhtml
OMDICTS['complex1'] = {}
OMDICTS['complex1']['complex_cartesian'] = oms_complex1_complex_cartesian

# interval1   http://www.openmath.org/cd/interval1.xhtml
OMDICTS['interval1'] = {}
OMDICTS['interval1']['integer_interval'] = oms_interval1_integer_interval

#integer1     http://www.openmath.org/cd/integer1.xhtml
OMDICTS['integer1'] = {}
OMDICTS['integer1']['factorial'] = oms_integer1_factorial

# list1    http://www.openmath.org/cd/list1.xhtml
OMDICTS['list1'] = {}
OMDICTS['list1']['list'] = oms_list1_list

# linalg2     http://www.openmath.org/cd/linalg2.xhtml
OMDICTS['linalg2'] = {}
OMDICTS['linalg2']['matrix'] = Matrix
OMDICTS['linalg2']['matrixrow'] = MatrixRow 


###############################################################
def parse_oms(node):
    """ Parses a OpenMath Symbol node.

    Looks up the OpenMath content dictionaries for the correct
    function for parsing the adjacent nodes.

    :param node: The XML node representing the OpenMath Symbol.
    :returns: The function to apply to the list of adjacent nodes.
    """
    return OMDICTS[node.get('cd')][node.get('name')]

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
    return elts[0](elts[1:len(elts)])

PARSE_OM_ELEMENT_HANDLER = {'OMI' : parse_omi, 'OMS' : parse_oms, 'OMA' : parse_oma, 'OMF': parse_omf}

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
    return parse_om_element(root[0])


