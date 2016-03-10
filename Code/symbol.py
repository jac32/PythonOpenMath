""" Module containing a generic representation of OMS OpenMath Nodes

All Content Dictionaries in CDs should extend this class.
"""

import abc
from abc import *

import xml.etree.ElementTree as ET
Element = ET.Element
subelement = ET.SubElement

class Symbol(object):
    """ Abstract Class for representing an OMS node

    Provides template for adding additional Content Dictionaries
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

