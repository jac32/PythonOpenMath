def om_pretty_node(node, level=0, indent='\t'):
    """ Pretty prints the string representation of the object
    
    Creates a formatted string containing the OpenMath XML
    representation of the given object and outputs it to 
    std out

    :params node: The object to be encoded to the string
    :param level: the level of nesting
    """
    str_ = string_indent(level=level, indent=indent)
    str_ += '<' + node.tag + attrib_string(node) 
    children = node.findall('*')

    if (node.text or children):
        str_ += '> '

        for child in children:
            str_ += '\n' + om_pretty_node(child, level+1, indent)
        if node.text:
            str_ += node.text + ' ' + close_tag(node)
        else:
            str_ += '\n' + string_indent(level, indent) + close_tag(node)
    else:
        str_ += '/>'    

    return str_ 

def close_tag(node):
    """This function produces the closing tag for the given node

    :param node: the node for the closing tag to be produced
    :return the string representation of the closing tag for the node
    """
    return '</' + node.tag + '>'

def string_indent(level=1, indent='\t'):
    """Indents the line to correspond with the current level of nesting
   
    :param level: the level of nesting for the current node
    :param indent: the much to indent based upon the nested
    :return the correct amount of white space for the node to be indented 
    """
    str_ = ''
    for i in range(0, level):
        str_ += indent
    return str_

def attrib_string(node):
    """Produces the attributes for the given node

    :param node: the node to have the attributes produced for
    :return the string representing the attributes for the node
    """
    str_ = ''
    for attrib in node.attrib:
        str_ = ' '
        str_ += attrib
        str_ += '='
        str_ += node.attrib[attrib]
    return str_
