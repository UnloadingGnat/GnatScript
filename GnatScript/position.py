##
# Position
# @author UnloadingGnat
# @date 2022-03-18
# v 0.1.0

class Position:
    def __init__(self, index, line, column, fileName, fileText):
        self.index = index;
        self.line = line
        self.column = column
        self.fileName = fileName
        self.fileText = fileText

    def advance(self, currentChar):
        self.index += 1
        self.column += 1

        if currentChar == '\n':
            self.line += 1
            self.column += 0
        
        return self
    
    def copy(self):
        return Position(self.index, self.line, self.column, self.fileName, self.fileText)
