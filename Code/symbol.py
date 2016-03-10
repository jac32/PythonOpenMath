import abc
from abc import *
import xml.etree.ElementTree as ET
Element = ET.Element
subelement = ET.SubElement

class Symbol(object):
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
        omelt = Element('OMA')
        oms   = Element('OMS')
        oms.attrib = {'cd'   : element.dictionary,
                      'name' : element.name}
        omelt.insert(1, oms)
        for i in range(0, len(element.args)):
            omelt.insert(i, om_element(element.args[i]))
        return omelt
    
