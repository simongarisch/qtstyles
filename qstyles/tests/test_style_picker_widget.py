'''
test the StylePickerWidget class
'''
from qstyles import StylePicker, StylePickerWidget


def test_displayed_styles(qtbot):
    ''' test that all of the available styles are displayed '''
    picker = StylePicker()
    picker_widget = StylePickerWidget()
    qtbot.addWidget(picker_widget)
    available_styles = sorted(picker.available_styles)
    displayed_styles = sorted([picker_widget.itemText(i)
                               for i in range(picker_widget.count())])
    assert available_styles == displayed_styles


def test_change_app_style(qtbot):
    ''' check that the style gets updated '''
    picker_widget = StylePickerWidget()
    qtbot.addWidget(picker_widget)
    text = picker_widget.itemText(0)
    picker_widget.setCurrentIndex(0)
    assert picker_widget.currentText() == text
        