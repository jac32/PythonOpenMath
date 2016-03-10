from os.path import dirname, basename, isfile
from symbol import Symbol
from collections import defaultdict
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f)]


################################################################
#
# OpenMath content dictionaries
#
