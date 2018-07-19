[![Build Status](https://travis-ci.org/simongarisch/qtstyles.svg?branch=master)](https://travis-ci.org/simongarisch/qtstyles)

[![Coverage Status](https://coveralls.io/repos/github/simongarisch/qtstyles/badge.svg?branch=master)](https://coveralls.io/github/simongarisch/qtstyles?branch=master)

# qtstyles
A collection of Qt Style Sheets accompanied by useful classes. **Two ways** to change your Qt application style sheet:

## 1. With the StylePicker class

View available styles with:
```python
from qtstyles import StylePicker

StylePicker().available_styles
```

And change the Qt application style using the get_sheet() method:
```python
from qtpy import QtWidgets
from qtstyles import StylePicker

app = QtWidgets.QApplication([])
win = QtWidgets.QMainWindow()
app.setStyleSheet(StylePicker("qdark").get_sheet()) # <-- changing the style here
win.show()
app.exec_()
```

## 2. We can also change the style sheet with an instance of StylePickerWidget (inherits from QComboBox)
```python
from qtpy import QtWidgets
from qtstyles import StylePickerWidget

app = QtWidgets.QApplication([])
win = QtWidgets.QMainWindow()
picker_widget = StylePickerWidget() # <-- this QComboBox allows the user to change style sheets
win.setCentralWidget(picker_widget)
win.show()
app.exec_()
```

See the 'Overview Notebook.ipynb' for additional details.

## Motivation
When looking for Qt ('.qss') style sheets most were scattered across different sites. 
Disclaimer: I've collected these style sheets from different repositories and they are not my own work.
Attribution, links and the associated licenses have been provided at the top of each qss file.
If you'd like to add a style sheet please create a pull request and I'll be happy to take a look.

## What does it look like
The StylePickerWidget is in the bottom left hand side of this window:
![qstyles demo](https://github.com/simongarisch/qstyles/blob/master/demo.PNG)
