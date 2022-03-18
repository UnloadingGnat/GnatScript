##
# Error
# @author UnloadingGnat
# @date 2022-03-18
# v 0.1.0

from colorama import Fore

class Error:
    def __init__(self, errorStart, errorEnd, errorName, details):
        self.errorStart = errorStart
        self.errorEnd = errorEnd
        self.errorName = errorName
        self.details = details

    def toString(self):
        return f'{self.errorName}: {self.details} File {self.errorStart.fileName}, Line {self.errorStart.line}, Column {self.errorStart.column}'


class IllegalCharError(Error):
    def __init__(self,errorStart, errorEnd, details):
        super().__init__(errorStart, errorEnd, 'Illegal Character', details)

