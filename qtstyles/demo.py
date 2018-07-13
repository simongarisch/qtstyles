from PyQt5 import QtWidgets
from .loader import get_style_sheets

def run_demo():
    style_sheets = get_style_sheets()
    
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

    app.setStyleSheet(style_sheets[1].read())
    app.exec_()


def main():
    run_demo()

if __name__ == "__main__":
    main()
