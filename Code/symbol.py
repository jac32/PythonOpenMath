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

    @staticmethod
    def eval(variables={}):
        raise EvaluationNonsenicalError(self)

