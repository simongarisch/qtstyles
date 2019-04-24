'''
Qt based functionality such as the StylePickerWidget and run_demo
will not be imported if qtpy is not installed.
'''

import os
import warnings
import random

try:
    from qtpy import QtWidgets, QtCore
except ImportError:
    warnings.warn("qtstyles Qt functionality requires qtpy to be installed.", ImportWarning)
else:
    from .demo import run_demo
    from .widget import StylePickerWidget

from .sheet import Sheet, get_style_sheets
from .picker import StylePicker
