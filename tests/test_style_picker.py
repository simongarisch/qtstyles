'''
Test the StylePicker class.
'''
import pytest
from qtstyles import errors, StylePicker


class TestStylePicker(object):
    ''' The style picker class allows us to pick a style
        and fetch the associated style sheet.
    '''

    def setup_method(self, method):
        ''' Use the default.qss sheet as a base case. '''
        self.picker = StylePicker()

    def teardown_method(self, method):
        ''' Delete attributes. '''
        del self.picker

    def test_default_style(self):
        ''' The style should be 'default' if none is provided. '''
        assert self.picker.style == "default"

    def test_get_sheet(self):
        ''' The sheet contents should be a string. '''
        contents = self.picker.get_sheet()
        assert isinstance(contents, str)

    def test_available_styles(self):
        ''' The available_styles attribute should be a list of strings. '''
        available_styles = self.picker.available_styles
        assert isinstance(available_styles, list)
        checks_list = [isinstance(item, str) for item in available_styles]
        assert False not in checks_list

    def test_style_attribute(self):
        ''' Check on setting / getting style. '''
        style = self.picker.available_styles[0]  # get the first style
        picker = StylePicker()
        picker.style = style
        assert picker.style == style  # check the style attribute has changed
        assert isinstance(picker.get_sheet(), str)  # which has a valid sheet
        # we shouldn't be able to set a style that doesn't exist
        with pytest.raises(errors.StyleDoesntExistError):
            picker.style = "not a valid style!"
