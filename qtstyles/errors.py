'''
Here we'll define exceptions to raise in the qtstyles package
'''

class QtStylesError(Exception):
    """ Base-class for all exceptions raised by this module. """


class SheetPathTypeError(QtStylesError):
    ''' The style sheet path must be a string '''
    def __init__(self):
        super(SheetPathTypeError, self).__init__("The style sheet path must be a string!")


class SheetPathValueError(QtStylesError):
    ''' The style sheet path end in '.qss' '''
    def __init__(self):
        super(SheetPathValueError, self).__init__("The style sheet path must end in '.qss'!")


class SheetPathFileDoesntExist(QtStylesError):
    ''' The style sheet path must point to a file that exists '''
    def __init__(self):
        super(SheetPathFileDoesntExist, self).__init__("No file exists at the path specified!")


class StyleDoesntExistError(QtStylesError):
    ''' The provided style sheet path must exist '''
    def __init__(self):
        super(StyleDoesntExistError, self).__init__("The requested style does not exist!")
