# PythonOpenMath
Basic support for the OpenMath standard in Python

## Documentation
Documentation is auto-generated using the Sphinx documentation tool.

Provided the style of docstring matches that below, the documentation
for the currently indexed files can be generated via a Makefile in the 
Docs folder.

To build the html format of the docs simply run `$ make html` 

### Docstring Example

``` python
	def ParseOMI(node):
		""" Parses a basic OpenMath integer node

	    Translates between the OpenMath XML representation of an integer,
		i.e. an OMI node, and a Python integer

	    :param node: The OMI XML node object
		:returns: The integer value of the node
		:rtype: int
		"""
    return int(node.text)
```
