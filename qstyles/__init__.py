try:
    from qtpy import QtWidgets # requires qtpy
except ImportError:
    warnings.warn("qstyles run_demo and StylePickerWidget requires qtpy to be installed.")
else:
    from .demo import run_demo
    from .widget import StylePickerWidget

from .loader import StylePicker