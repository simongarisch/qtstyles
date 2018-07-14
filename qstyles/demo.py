import warnings
from loader import StylePicker
try:
    from qtpy import QtWidgets # requires qtpy
except ImportError:
    warnings.warn("qstyles basic demo requires qtpy")


def run_demo(style="default"):
    ''' pick a style to run with this basic example '''
    picker = StylePicker()
    
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
    grid.addWidget(QtWidgets.QLineEdit(), 0, 1)
    grid.addWidget(QtWidgets.QLineEdit(), 1, 1)
    grid.addWidget(QtWidgets.QPushButton("Submit"), 2, 1)
    win.show()

    app.setStyleSheet(StylePicker(style).get_sheet())
    app.exec_()


def main():
    run_demo()

if __name__ == "__main__":
    main()
