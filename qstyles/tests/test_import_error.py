import sys
import pytest


class TestImportError(object):
    ''' When importing this package (and running __init__) 
        you'll get an import error if qtpy is not installed '''
    
    def remove_qstyles_import(self):
        # remove the qstyles if it has been loaded
        if "qstyles" in sys.modules:
            del sys.modules["qstyles"]
    
    def test_import_error(self):
        # test that the absence of anyqt raises a warning
        self.remove_qstyles_import()
        sys.modules["qtpy"] = None
        with pytest.warns(ImportWarning):
            import qstyles
        self.remove_qstyles_import()
        
    