"""Util initialization

makes the Util modules from Crypto AND CryptoPlus available here
"""
from __future__ import absolute_import
#import Crypto
#from Crypto.Util import number, randpool, RFC1751
from . import padding, util, python_compat, number, RFC1751 #, randpool

from pkg_resources import parse_version

__all__ = ["padding","util","number","RFC1751","python_compat"] #,"randpool"

#if parse_version(Crypto.__version__) > parse_version("2.0.1"):
#        from Crypto.Util import python_compat
#        __all__.append("python_compat")

#del Crypto
