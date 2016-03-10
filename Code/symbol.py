import abc
from abc import *
import xml.etree.ElementTree as ET
Element = ET.Element
subelement = ET.SubElement

class Symbol(object):
    """Generic super class for all OMS OpenMath nodes.
    It has a generic implementation for encoding to OpenMath, as well
    as abstract methods that serve as properties that its children implement
    """
    __metaclass__ = ABCMeta

    _args = []
    
    @property
    def args(self):
        return self._args

    @args.setter
    def args(self, newargs):
        self._args = newargs
    
    @abstractmethod
    def name():
        return 

    @abstractmethod
    def dictionary():
        return 

    def eval(variables={}):
        raise EvaluationNonsenicalError(self)
    
    def put(element):
        """Encodes the given element into OpenMath XML.
        It recursively calls om_element on each child of the OMS to produce
        the correct nesting for XML
        
        :param element: the element to be encoded
        :return the OpenMath OMA element detailing this particular symbol
        """
        omelt = Element('OMA')
        oms   = Element('OMS')
        oms.attrib = {'cd'   : element.dictionary,
                      'name' : element.name}
        omelt.insert(1, oms)
        for i in range(0, len(element.args)):
            omelt.insert(i, om_element(element.args[i]))
        return omelt
    
