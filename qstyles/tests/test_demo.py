import pytest
import pytestqt
import threading
import time
from qtpy import QtWidgets
from qstyles import run_demo


class TestDemo(object):
    ''' Our demo allows us to see the effect of selecting different styles. 
        Here we'll do so at random.
    '''
    def test_demo(self):
        # Show the demo for x seconds whilst randomly selecting style sheets
        run_demo(close_after=10, auto_test=True)