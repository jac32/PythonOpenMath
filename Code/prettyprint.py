def om_pretty_node(node, level=0, indent='\t'):
    """ Pretty prints the string representation of the object
    
    Creates a formatted string containing the OpenMath XML
    representation of the given object and outputs it to 
    std out

    :params x: The object to be encoded to the string
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
    return '</' + node.tag + '>'
        
    # if children == []:
    #     if node.text != None: print(node.text, end=' ')
    # elif node.text == None :
    #     print()
    #     print_indent(level, indent=indent)
        
    # print('</' + node.tag, end='>')

    # if level == 0: print()


def string_indent(level=1, indent='\t'):
    str_ = ''
    for i in range(0, level):
        str_ += indent
    return str_

def attrib_string(node):
    str_ = ''
    for attrib in node.attrib:
        str_ = ' '
        str_ += attrib
        str_ += '='
        str_ += node.attrib[attrib]
    return str_
