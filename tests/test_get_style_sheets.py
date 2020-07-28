'''
Testing the get_style_sheets function.
'''
import os
from qtstyles import get_style_sheets, Sheet


class TestGetStyleSheets(object):
    ''' The get_style_sheets() function gets a list of styles
        and their associated sheet objects. '''

    def setup_method(self, method):
        ''' Run the get_style_sheets function and store results. '''
        self.results_dict = get_style_sheets()

    def teardown_method(self, method):
        ''' Clear attributes. '''
        del self.results_dict

    def test_all_keys(self):
        ''' Test that all of the keys (style sheet names)
            are or the type str.
        '''
        checks_list = [isinstance(key, str) for key in self.results_dict]
        assert False not in checks_list

    def test_all_values(self):
        ''' All of the values should be instance of Sheet. '''
        checks_list = [
            isinstance(value, Sheet)
            for value in self.results_dict.values()
        ]
        assert False not in checks_list

    def test_sheet_files_exist(self):
        ''' All of the sheet instance should point to
            '.qss' files that exist.
        '''
        paths_list = [value.path for value in self.results_dict.values()]
        checks_list = [os.path.isfile(path) for path in paths_list]
        assert False not in checks_list
