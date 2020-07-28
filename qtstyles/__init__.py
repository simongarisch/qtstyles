'''
Qt based functionality such as the StylePickerWidget and run_demo
will not be imported if qtpy is not installed.
'''
import warnings

try:
    from qtpy import QtWidgets, QtCore  # noqa: F401
except ImportError:
    warnings.warn(
        "qtstyles Qt functionality requires qtpy to be installed.",
        ImportWarning
    )
else:
    from .demo import run_demo  # noqa: F401
    from .widget import StylePickerWidget  # noqa: F401

from .sheet import Sheet, get_style_sheets  # noqa: F401
from .picker import StylePicker  # noqa: F401
