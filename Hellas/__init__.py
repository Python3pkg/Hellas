__version__ = "0.1.1"
__author__ = "nickmilon"

from sys import version_info

_PY_VERSION = version_info
_IS_PY2 = (_PY_VERSION[0] == 2)
_IS_PY3 = (_PY_VERSION[0] == 3)