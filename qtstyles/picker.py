'''
Defines StylePicker: a class that allows us to pick style sheets and collect their
style sheet contents with get_sheet()
'''

from qtstyles import errors
from qtstyles.sheet import get_style_sheets


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
        ''' returns a string containing the style sheet for our chosen style '''
        return self.sheets[self.style].contents

    @property
    def style(self):
        ''' gets the current selected style '''
        return self._style

    @style.setter
    def style(self, style):
        ''' sets the current style which must be in the available_styles list '''
        if style not in self.available_styles:
            raise errors.StyleDoesntExistError
        self._style = style

    @property
    def available_styles(self):
        ''' returns a list of all available styles we can choose from
            Note that dict.keys() will return a list in py2 but a dict_keys object in py3 '''
        return list(self.sheets.keys())
