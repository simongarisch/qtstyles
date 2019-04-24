'''
Includes a run_demo() function that acts as a basic demo for our
StylePicker and StylePickerWidget classes
'''

import random
from qtpy import QtWidgets, QtCore
from qtstyles.picker import StylePicker
from qtstyles.widget import StylePickerWidget


def run_demo(close_after=None, auto_test=False):
    '''
    Args:
    close_after: either None or integer. Number of seconds
    after which the demo will close
    auto_test: boolean. If true then randomly select a style at intervals.

    This function provides a demonstration in changing the application style sheet.
    1) The first option is to set the style sheet once with
       app.setStyleSheet(StylePicker("default").get_sheet())
    2) The second option is to include a style picker widget (QComboBox) that'll
       change the application style sheet when a new style is selected
       grid.addWidget(StylePickerWidget(), 2, 0)
    '''

    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication([])

    win = QtWidgets.QMainWindow()
    win.setWindowTitle("Style Sheets")

    frame = QtWidgets.QFrame()
    win.setCentralWidget(frame)

    grid = QtWidgets.QGridLayout(frame)
    grid.setHorizontalSpacing(5)
    grid.setVerticalSpacing(5)
    grid.addWidget(QtWidgets.QLabel("Username"), 0, 0)
    grid.addWidget(QtWidgets.QLabel("Password"), 1, 0)
    user_input = QtWidgets.QLineEdit()
    pass_input = QtWidgets.QLineEdit()
    grid.addWidget(user_input, 0, 1)
    grid.addWidget(pass_input, 1, 1)

    picker_widget = StylePickerWidget()
    grid.addWidget(picker_widget, 2, 0)
    grid.addWidget(QtWidgets.QPushButton("Submit"), 2, 1)
    win.show()

    def choose_random_style():
        ''' select a random style from the picker_widget '''
        style_list = StylePicker().available_styles
        chosen_style = random.choice(style_list)
        picker_widget.setCurrentIndex(picker_widget.findText(chosen_style))

    def close_demo():
        ''' close the demo once 'close_after' seconds have elapsed '''
        win.close()

    if auto_test:
        timer = QtCore.QTimer()
        timer.timeout.connect(choose_random_style)
        timer.start(1000)

    if isinstance(close_after, int):
        close_timer = QtCore.QTimer()
        close_timer.singleShot(close_after * 1000, close_demo) # seconds * 1000 = milliseconds

    app.setStyleSheet(StylePicker("default").get_sheet())
    app.exec_()

"""
def main():
    ''' testing our run_demo function '''
    run_demo(close_after=10, auto_test=True)

if __name__ == "__main__":
    main()
"""