##
# Lexer
# @author UnloadingGnat
# @date 2022-03-18
# v 0.1.0

from gnatScript.token import GST_DIV, GST_FLOAT, GST_INT, GST_LPAREN, GST_MINUS, GST_MUL, GST_PLUS, GST_RPAREN, Token
from gnatScript.error import IllegalCharError
from gnatScript.position import Position

##############################
# Constants
##############################
NUMBERS = '0123456789'


class Lexer:
    def __init__(self, fileName, text):
        self.fileName = fileName
        self.text = text
        self.pos = Position(-1, 0, -1, fileName, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        if self.pos.index < len(self.text):
            self.current_char = self.text[self.pos.index]
        else:
            self.current_char = None

    def createTokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in NUMBERS:
                tokens.append(self.createNumber())
            elif self.current_char == '+':
                tokens.append(Token(GST_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(GST_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(GST_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(GST_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(GST_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(GST_RPAREN))
                self.advance()
            else:
                errorStart = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(errorStart, self.pos,"'" + char + "'")

            
        return tokens, None

    def createNumber(self):
        numString = ''
        decimal = 0

        while self.current_char != None and self.current_char in NUMBERS + '.':
            if self.current_char == '.':
                if decimal == 1:
                    break
                decimal += 1
                numString += '.'
            else:
                numString += self.current_char
            self.advance()

        if decimal == 0:
            return Token(GST_INT, int(numString))
        else:
            return Token(GST_FLOAT, float(numString))