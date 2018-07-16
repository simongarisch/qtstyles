import pytest
import pytestqt
import threading
import time
from qtpy import QtWidgets
from qstyles import run_demo

"""
class HelperThread(threading.Thread):
    ''' We can't leave the demo window open ...
        This thread will check for an application instance and call close()
    '''
    def __init__(self):
        # set daemon to True and start the thread
        super(HelperThread, self).__init__()
        self.daemon = True
        self.start()
        
    def run(self):
        while True:
            app = QtWidgets.QApplication.instance()
            if app is not None:
                app.closeAllWindows()
            time.sleep(1)
"""

class TestDemo(object):
    
    def test_demo(self):
        thread = HelperThread() # this will call close on the demo
        run_demo()