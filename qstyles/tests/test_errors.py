import pytest
from qstyles import errors

class TestErrors(object):
    ''' testing the errors module for this package '''

    def test_errors(self):
        ''' make sure these can all be raised without issue '''    
        errors_list = [errors.QStylesError,
                       errors.SheetPathTypeError,
                       errors.SheetPathValueError,
                       errors.StyleDoesntExistError]
        
        for error in errors_list:            
            # make sure there is no problem raising the error
            with pytest.raises(error):
                raise error