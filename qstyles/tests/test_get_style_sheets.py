'''
testing the get_style_sheets function
'''
import os
from qstyles import get_style_sheets, Sheet


class TestGetStyleSheets(object):
    ''' the get_style_sheets() function gets a list of styles
        and their associated sheet objects '''

    def setup_method(self, method):
        ''' run the get_style_sheets function and store results '''
        self.results_dict = get_style_sheets()

    def teardown_method(self, method):
        ''' clear attributes '''
        del self.results_dict

    def test_all_keys(self):
        ''' test that all of the keys (style sheet names) are or the type str '''
        checks_list = [isinstance(key, str) for key in self.results_dict]
        assert False not in checks_list

    def test_all_values(self):
        ''' all of the values should be instance of Sheet '''
        checks_list = [isinstance(value, Sheet) for value in self.results_dict.values()]
        assert False not in checks_list

    def test_sheet_files_exist(self):
        ''' all of the sheet instance should point to '.qss' files that exist '''
        paths_list = [value.path for value in self.results_dict.values()]
        checks_list = [os.path.isfile(path) for path in paths_list]
        assert False not in checks_list
        