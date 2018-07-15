import os
import pytest
from qstyles import errors, Sheet

class TestSheet(object):
    ''' each of the style sheets are represented as sheet objects (which we'll test here) '''
    
    def setup_method(self, method):
        # use the default.qss sheet as a base case
        dirpath = os.path.dirname(os.path.abspath(__file__))
        path = self.path = os.path.join(dirpath, "..", "style sheets", "default.qss")
        self.sheet = Sheet(path)
        
    def teardown_method(self, method):
        # delete the TestSheet instance attributes
        del self.path
        del self.sheet
    
    def test_init(self):
        # check that the sheet has a correct path and contents
        assert self.sheet.path == self.path
        assert isinstance(self.sheet.contents, str)
        
    def test_path_is_string(self):
        # all sheet paths must be a string
        with pytest.raises(errors.SheetPathTypeError):
            Sheet(path=42)
        
    def test_path_ends_qss(self):
        # all sheet paths must end with '.qss'
        with pytest.raises(errors.SheetPathValueError):
            Sheet(path="default")
            
    def test_path_must_exist(self):
        # all sheet paths must point to a file
        with pytest.raises(errors.SheetPathFileDoesntExist):
            Sheet(path=self.path.replace("default.qss", "not_a_sheet.qss"))