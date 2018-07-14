import os
import errors # defines errors for this package

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
        if not path.endswith(".qss"):
            raise errors.NotValidSheetError
        self._path = path
        self._contents = None # to be loaded on request
        
    @property
    def path(self):
        return self._path
    
    @property
    def contents(self):
        if self._contents is None:
            self._load_contents()
        return self._contents
    
    def _load_contents(self):
        # loads the style sheet contents (if not already loaded)
        with open(self.path, "r") as f:
            self._contents = f.read()
            

def get_style_sheets():
    '''
    Returns a dictionary with the style sheet names as keys and
    associated Sheet objects as values
    There must be a sheet called 'default' which is empty.
    >>> sheets = get_style_sheets()
    >>> isinstance(sheets, dict) # returns a dictionary
    True
    >>> first_sheet_name = sheets.keys()[0]
    >>> first_sheet_object = sheets[first_sheet_name]
    >>> first_sheet_object.path.endswith(".qss") # these should all be .qss files
    True
    >>> "default" in sheets.keys() # there should be a 'default.qss' sheet available
    True
    '''
    dirpath = os.path.dirname(os.path.abspath(__file__))
    
    sheets = {}
    for name in os.listdir(os.path.join(dirpath, "style sheets")):
        path = os.path.join(dirpath, "style sheets", name)
        sheets[name.replace(".qss", "")] = Sheet(path)
    return sheets


class StylePicker(object):
    '''
    Returns a string containing the style sheet contents for a requested style name.
    'sheets' is a class attribute that'll act as a shared resource for all StylePicker
    objects. There is no point fetching the sheets data multiple times as it is static.
    
    '''
    sheets = get_style_sheets()
    
    def __init__(self, style ="default"):
        self.style = style

    def get_sheet(self):
        return self.sheets[self.style].contents

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, style):
        if style not in self.available_styles:
            raise errors.StyleDoesntExistError
        self._style = style

    @property
    def available_styles(self):
        return self.sheets.keys()
    
    
def main():
    sheets = get_style_sheets()
    print(sheets)

if __name__ == "__main__":
    main()
