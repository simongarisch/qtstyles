'''
Test the Sheet class.
'''
import os
import pytest
from qtstyles import errors, Sheet


def test_init():
    ''' Check that the sheet has a correct path and contents. '''
    dirpath = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(
        dirpath, "..", "qtstyles", "style_sheets", "default.qss"
    )
    sheet = Sheet(path)
    assert sheet.path == path
    assert isinstance(sheet.contents, str)


def test_path_is_string():
    ''' All sheet paths must be a string. '''
    with pytest.raises(errors.SheetPathTypeError):
        Sheet(path=42)


def test_path_ends_qss():
    ''' All sheet paths must end with '.qss'. '''
    with pytest.raises(errors.SheetPathValueError):
        Sheet(path="default")


def test_path_must_exist():
    ''' All sheet paths must point to a file. '''
    with pytest.raises(errors.SheetPathFileDoesntExist):
        Sheet(path="not_a_sheet.qss")
