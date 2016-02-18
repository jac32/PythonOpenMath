""" Parsing OpenMath objects

This module provides a number of functions for decoding "objects"
from the parsed XML tree.

"""

################################################################
#
# Basic OpenMath elements
#


def ParseOMI(node):
    """ Parses a basic OpenMath integer node

    Translates between the OpenMath XML representation of an integer,
    i.e. an OMI node, and a Python integer

    :param node: The OMI XML node object
    :returns: The integer value of the node
    :rtype: int
    
    """
    return int(node.text)
    

################################################################
#
# OpenMath content dictionaries
#
omdicts = {}

# list1    http://www.openmath.org/cd/list1.xhtml
omdicts['list1'] = {}

# list1.list
def oms_list1_list(list):
    return list

omdicts['list1']['list'] = oms_list1_list


# logic1	http://www.openmath.org/cd/logic1.xhtml
omdicts['logic1'] = {}

# logic1.true
omdicts['logic1']['true'] = True


###############################################################
def ParseOMS(node):
    """ Parses a OpenMath Symbol node
    Looks up the OpenMath content dictionaries for the correct 
    function for parsing the adjacent nodes.

    :param node: The XML node representing the OpenMath Symbol
    :returns: The function to apply to the list of adjacent nodes
    """
    return omdicts[ node.get('cd') ][ node.get('name') ]

def ParseOMA(node):
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
    48
    """
    return ParseOMelement(root[0])


################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
