'''
test the qstyles run_demo function
'''
from qstyles import run_demo


def test_demo_auto_test():
    ''' Show the demo for x seconds whilst randomly selecting style sheets '''
    run_demo(close_after=5, auto_test=True)
