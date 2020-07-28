'''
Test that all of the errors are getting raised correctly.
'''
import pytest
from qtstyles import errors


def test_errors():
    ''' Make sure these can all be raised without issue. '''
    errors_list = [errors.QtStylesError,
                   errors.SheetPathTypeError,
                   errors.SheetPathValueError,
                   errors.StyleDoesntExistError]

    for error in errors_list:
        # make sure there is no problem raising the error
        with pytest.raises(error):
            raise error
