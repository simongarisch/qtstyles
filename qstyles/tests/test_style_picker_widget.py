import os
import pytest
import pytestqt
from qtpy import QtWidgets
from qstyles import StylePicker, StylePickerWidget


class TestStylePickerWidget(object):
    
    def setup_method(self, method):
        self.picker = StylePicker()
        self.picker_widget = StylePickerWidget()
        
    def teardown_method(self, method):
        # clear the attributes
        del self.picker
        
    def test_init(self, qtbot):
        qtbot.addWidget(self.picker_widget)
        style_count = self.picker.
        assert isinstance(self.picker, QtWidgets.QComboBox)
        