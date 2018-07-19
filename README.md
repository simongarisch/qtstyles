# qtstyles
## What is it?
A collection of Qt Style Sheets accompanied by useful classes. Provided are two ways to change your Qt application style sheet:

* With the StylePicker class...
```python
s = "Python syntax highlighting"
print s
```

* StylePicker: pick a style and get the style sheet with 'get_sheet()'. the 'available_styles' attribute returns a list of available styles.
* StylePickerWidget (inherits from QComboBox): pick a style from the widget and you application style sheet will update.

See the 'Overview Notebook.ipynb' for additional details.

## Motivation?
When looking for qt ('.qss') style sheets most were scattered across different sites. 
Disclaimer: I've collected these style sheets from different repositories and they are not my own work.
Attribution, links and the associated licenses have been provided at the top of each qss file.
If you'd like to add a style sheet please create a pull request and I'll be happy to take a look.

## What does it look like?
The StylePickerWidget is in the bottom left hand side of the window:
![qstyles demo](https://github.com/simongarisch/qstyles/blob/master/demo.PNG)