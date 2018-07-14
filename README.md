# qstyles
## What is it?
A collection of Qt Style Sheets accompanied by:
* class StylePicker: pick style sheets and collect their contents with 'get_sheet()'.
* class StylePickerWidget: (inherits from QComboBox) select a style and the application will update to the selected style sheet.

See the 'Overview Notebook.ipynb' for additional details.

## Motivation?
When looking for qt ('.qss') style sheets most were scattered across different sites. 
Disclaimer: I've collected these style sheets from different repositories and they are not my own work.
Attribution, links and the associated licenses have been provided at the top of each qss file.
If you'd like to add a style sheet please create a pull request and I'll be happy to take a look.

## What does it look like?
The StylePickerWidget is in the bottom left hand side of the window:
![qstyles demo](https://github.com/simongarisch/qstyles/blob/master/demo.PNG)