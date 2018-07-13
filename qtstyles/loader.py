import os

class Sheet(object):
    '''
    Keeps key information related to style sheets, particularly the path
    and contents as a string.
    >>> import os
    >>> path = os.path.join("style_sheets", "default.qss")
    >>> sheet = Sheet(path)
    >>> sheet.load_contents()
    >>> isinstance(sheet.contents, str)
    True
    '''
    def __init__(self, path):
        self._path = path
        self._contents = None # to be loaded on request
        
    @property
    def path(self):
        return self._path
    
    @property
    def contents(self):
        return self._contents
    
    def load_contents(self):
        # loads the style sheet contents (if not already loaded)
        if self.contents is None:
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
    >>> first_sheet_object = sheets[first_sheet_name][0]
    >>> first_sheet_object.path.endswith(".qss") # these should all be .qss files
    True
    >>> "default" in sheets.keys() # there should be a 'default.qss' sheet available
    True
    '''
    dirpath = os.path.dirname(os.path.abspath(__file__))
    
    sheets = {}
    for sheet_name in os.listdir(os.path.join(dirpath, "style sheets")):
        sheet_path = os.path.join(dirpath, sheet_name)
        sheets[sheet_name.replace(".qss", "")] = [sheet_path, None]
    return sheets


class StylePicker(object):
    '''
    Returns a string containing the style sheet contents for a requested style name.
    'sheets' is a class attribute that'll act as a shared resource for all StylePicker
    objects. There is no point fetching the sheets data multiple times as it is static.
    
    '''
    sheets = get_style_sheets()
    
    def __init__(self, style_name="default"):
        pass
    
    


def main():
    sheets = get_style_sheets()
    print(sheets)

if __name__ == "__main__":
    main()
