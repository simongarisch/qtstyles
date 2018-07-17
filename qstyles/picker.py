import errors
from sheet import get_style_sheets

'''
Defines StylePicker: a class that allows us to pick style sheets and collect their 
    style sheet contents with get_sheet()
'''

class StylePicker(object):
    '''
    The StylePicker class has the following properties:
      style: the current selected style
      available_styles: a list of strings representing all of the styles available
      
    And the following methods:
      __init__(style='default'): the constructor takes one argument being the selected style
      get_sheet(): returns a string being the style sheet contents for our selected style
      
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
