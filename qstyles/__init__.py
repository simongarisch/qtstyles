import warnings
import random

try:
    from qtpy import QtWidgets, QtCore # requires qtpy
except ImportError:
    warnings.warn("qstyles run_demo and StylePickerWidget requires qtpy to be installed.", ImportWarning)
else:
    from .demo import run_demo
    from .widget import StylePickerWidget

from .sheet import Sheet, get_style_sheets
from .picker import StylePicker