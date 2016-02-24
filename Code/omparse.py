""" Parsing OpenMath Objects
=============================

This module provides a number of functions for decoding "objects"
from the parsed XML tree.

"""

################################################################
#
# Basic OpenMath elements
#


def ParseOMI(node):
    """ Parses a basic OpenMath integer node.

    Translates between the OpenMath XML representation of an integer,
    i.e. an OMI node, and a Python integer.

    :param node: The OMI XML node object.
    :returns: The integer value of the node.
    :rtype: int
    
    """
    return int(node.text)
    

################################################################
#
# OpenMath content dictionaries
#
omdicts = {}

# interval1   http://www.openmath.org/cd/interval1.xhtml
omdicts['interval1'] = {}

def oms_interval1_integer_interval(list):
    if (len(list) == 2):
        return range(list[0],list[1])

        
omdicts['interval1']['integer_interval'] = oms_interval1_integer_interval


# complex1    http://www.openmath.org/cd/complex1.xhtml
omdicts['complex1'] = {}

def oms_complex1_complex_cartesian(list):
    if (len(list) == 2):
        return complex(list[0],list[1])

omdicts['complex1']['complex_cartesian'] = oms_complex1_complex_cartesian



# nums1    http://www.openmath.org/cd/nums1.xhtml1
omdicts['nums1'] = {}

def oms_nums1_rational(list):
    if (len(list) == 2):
        return (list[0],list[1])

omdicts['nums1']['rational'] = oms_nums1_rational

# list1    http://www.openmath.org/cd/list1.xhtml
omdicts['list1'] = {}

# list1.list
def oms_list1_list(list):
    return list

omdicts['list1']['list'] = oms_list1_list


# logic1	http://www.openmath.org/cd/logic1.xhtml
omdicts['logic1'] = {}

# logic1.true
omdicts['logic1']['true'] = lambda x: True
omdicts['logic1']['false'] = lambda x: False

###############################################################
def ParseOMS(node):
    """ Parses a OpenMath Symbol node.

    Looks up the OpenMath content dictionaries for the correct 
    function for parsing the adjacent nodes.

    :param node: The XML node representing the OpenMath Symbol.
    :returns: The function to apply to the list of adjacent nodes.
    """
    return omdicts[ node.get('cd') ][ node.get('name') ]

def ParseOMA(node):
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
        elts.append( ParseOMelement(child) )
    # now the first element of 'elts' is a function to be applied to the rest of the list
    return elts[0](elts[1:len(elts)]) 

ParseOMelementHandler = { 'OMI' : ParseOMI, 'OMS' : ParseOMS, 'OMA' : ParseOMA }

def ParseOMelement(obj):
    """ Appropriately parses a OpenMath XML element
    
    Uses the `parseOMelementHandler` dictionary to fetch the correct parsing
    function based on the element's XML tag. 
    This allows for the ype of element to be identified and the subtree to be
    handled correctly.

    :param obj: The node of the tree to be parsed
    :returns: The python representation of the OpenMath XML subtree
    """
    return ParseOMelementHandler[obj.tag](obj)

def ParseOMroot(root):
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
    return ParseOMelement(root[0])


################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
