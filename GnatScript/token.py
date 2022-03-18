##
# Token
# @author UnloadingGnat
# @date 2022-03-18
# v 0.1.0

# Gnat Script Token
GST_INT = 'TT_INT'
GST_FLOAT = 'FLOAT'
GST_PLUS = 'PLUS'
GST_MINUS = 'MINUS'
GST_MUL = 'MUL'
GST_DIV = 'DIV'
GST_LPAREN = 'LPAREN'
GST_RPAREN = 'RPAREN'

class Token:
    """Tokenizer for GnatScript"""
    def __init__(self, tokenType, value=None):
        self.type = tokenType
        self.value = value

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'

