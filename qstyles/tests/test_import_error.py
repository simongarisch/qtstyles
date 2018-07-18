'''
test that we get an import warning if the user cannot import qtpy
'''
import sys
import pytest


def remove_qstyles_import():
    ''' remove the qstyles if it has been loaded '''
    if "qstyles" in sys.modules:
        del sys.modules["qstyles"]

def test_import_error():
    ''' test that the absence of anyqt raises a warning '''
    remove_qstyles_import()
    sys.modules["qtpy"] = None
    with pytest.warns(ImportWarning):
        import qstyles
    remove_qstyles_import()
    