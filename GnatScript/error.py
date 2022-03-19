##
# Error
# @author UnloadingGnat
# @date 2022-03-18
# v 0.1.0


class Error:
    """Error Handler For GnatScript"""
    def __init__(self, errorStart, errorEnd, errorName, details):
        self.errorStart = errorStart
        self.errorEnd = errorEnd
        self.errorName = errorName
        self.details = details

    def __str__(self):
        return f'{self.errorName}: {self.details}\nFile "{self.errorStart.fileName}", Line {self.errorStart.line}, Column {self.errorStart.column}'


class IllegalCharError(Error):
    def __init__(self,errorStart, errorEnd, details):
        super().__init__(errorStart, errorEnd, 'Illegal Character', details)

