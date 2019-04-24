'''
Defines the following ...

Sheet: a class representing a style sheet object with attributes such as path and contents

get_style_sheets: a function that returns a dictionary with style sheet names as keys and
sheet objects as values
'''

import os
from qtstyles import errors


class Sheet(object):
    '''
    Keeps key information related to style sheets, particularly the path
    and contents as a string.
    >>> import os
    >>> dirpath = os.path.dirname(os.path.abspath(__file__))
    >>> path = os.path.join(dirpath, "style_sheets", "default.qss")
    >>> sheet = Sheet(path)
    >>> isinstance(sheet.contents, str)
    True
    '''
    def __init__(self, path):
        ''' This constructor only takes one argument being the sheet path.
            path = the path to a qss file... must be a string and end with '.qss'
        '''
        if not isinstance(path, str):
            raise errors.SheetPathTypeError
        if not path.endswith(".qss"):
            raise errors.SheetPathValueError
        if not os.path.isfile(path):
            raise errors.SheetPathFileDoesntExist
        self._path = path
        self._contents = None # to be loaded on request

    @property
    def path(self):
        ''' collect the path as a sheet attribute '''
        return self._path

    @property
    def contents(self):
        ''' the style sheet contents will load only once when needed '''
        if self._contents is None:
            self._load_contents()
        return self._contents

    def _load_contents(self):
        ''' loads the style sheet contents (if not already loaded) '''
        with open(self.path, "r") as qss_file:
            self._contents = qss_file.read()


def get_style_sheets():
    '''
    Returns a dictionary with the style sheet names as keys and
    associated Sheet objects as values
    There must be a sheet called 'default' which is empty.
    >>> sheets = get_style_sheets()
    >>> isinstance(sheets, dict) # returns a dictionary
    True
    >>> sheet_object = sheets["default"] # there should be a 'default.qss' sheet available
    >>> sheet_object.path.endswith(".qss") # these should all be .qss files
    True
    '''
    dirpath = os.path.dirname(os.path.abspath(__file__))

    sheets = {}
    for name in os.listdir(os.path.join(dirpath, "style_sheets")):
        if "__" in name:
            # exclude any files with a double underscore (e.g. __init__, __pycache__)
            continue
        path = os.path.join(dirpath, "style_sheets", name)
        sheets[name.replace(".qss", "")] = Sheet(path)
    return sheets
