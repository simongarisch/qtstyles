'''
test that we get an import warning if the user cannot import qtpy
'''
import sys
import pytest


def remove_qtstyles_import():
    ''' remove the qtstyles if it has been loaded '''
    if "qtstyles" in sys.modules:
        del sys.modules["qtstyles"]

def test_import_error():
    ''' test that the absence of anyqt raises a warning '''
    remove_qtstyles_import()
    sys.modules["qtpy"] = None
    with pytest.warns(ImportWarning):
        import qtstyles
    remove_qtstyles_import()
    