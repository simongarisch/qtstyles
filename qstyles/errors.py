
class QStylesError(Exception):
    """ Base-class for all exceptions raised by this module. """


class NotValidSheetError(QStylesError):
    def __init__(self):
        super(NotValidSheetError, self).__init__("The style sheet path does not end in '.qss'!")


class StyleDoesntExistError(QStylesError):
    def __init__(self):
        super(StyleDoesntExistError, self).__init__("The requested style does not exist!")
