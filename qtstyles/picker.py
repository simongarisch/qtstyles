'''
Defines StylePicker: a class that allows us to pick style sheets
and collect their style sheet contents with get_sheet().
'''
from qtstyles import errors
from qtstyles.sheet import get_style_sheets


class StylePicker(object):
    '''
    The StylePicker class has the following properties:
    style: the current selected style.
    available_styles: a list of strings representing all available styles.

    And the following methods:
    __init__(style='default'): constructor.
    get_sheet(): returns the style sheet contents as a string.

    'sheets' is a class attribute that'll act as a shared resource
    for all StylePicker objects.
    '''
    sheets = get_style_sheets()

    def __init__(self, style="default"):
        self.style = style

    def get_sheet(self):
        ''' Returns a string containing the style sheet
            for our chosen style.
        '''
        return self.sheets[self.style].contents

    @property
    def style(self):
        ''' Gets the current selected style. '''
        return self._style

    @style.setter
    def style(self, style):
        ''' Sets the current style which must be in the
            available_styles list.
        '''
        if style not in self.available_styles:
            raise errors.StyleDoesntExistError
        self._style = style

    @property
    def available_styles(self):
        ''' Returns a list of all available styles to choose from. '''
        return list(self.sheets.keys())
