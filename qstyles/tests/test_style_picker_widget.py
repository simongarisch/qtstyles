import os
import pytest
import pytestqt
from qtpy import QtWidgets
from qstyles import StylePicker, StylePickerWidget


class TestStylePickerWidget(object):
        
    def test_displayed_styles(self, qtbot):
        # test that all of the available styles are displayed
        self.picker = StylePicker()
        self.picker_widget = StylePickerWidget()
        qtbot.addWidget(self.picker_widget)
        available_styles = sorted(self.picker.available_styles)
        displayed_styles = sorted([self.picker_widget.itemText(i) 
                                   for i in range(self.picker_widget.count())])
        assert available_styles == displayed_styles
        
    def test_change_app_style(self, qtbot):
        # check that the style gets updated
        self.picker = StylePicker()
        self.picker_widget = StylePickerWidget()
        qtbot.addWidget(self.picker_widget)
        text = self.picker_widget.itemText(0)
        self.picker_widget.setCurrentIndex(0)
        assert self.picker_widget.currentText == text
        # also check the app style sheet is changed
        