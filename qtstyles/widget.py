'''
Defines only the StylePickerWidget class which inherits from QComboBox
'''

from qtpy import QtWidgets
from qtstyles.picker import StylePicker


class StylePickerWidget(QtWidgets.QComboBox):
    ''' This QComboBox will allow the user to change the application
        style sheet on demand '''
    def __init__(self, parent=None):
        ''' constructor only takes the parent widget as an argument '''
        super(StylePickerWidget, self).__init__(parent)
        self.addItems(StylePicker().available_styles)
        self.setCurrentIndex(self.findText("default"))
        self.currentIndexChanged.connect(self.change_app_style)

    def change_app_style(self):
        ''' this method fires when a new style is selected '''
        style = self.currentText()
        app = QtWidgets.QApplication.instance()
        if app is not None:
            app.setStyleSheet(StylePicker(style).get_sheet())


"""
def main():
    ''' a quick demo of our StylePickerWidget class '''
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication([])

    win = QtWidgets.QMainWindow()
    win.setWindowTitle("Test StylePickerWidget")
    picker_widget = StylePickerWidget()
    win.setCentralWidget(picker_widget)
    win.show()
    app.exec_()

if __name__ == "__main__":
    main()
"""
