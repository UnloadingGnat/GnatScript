##
# Token
# @author UnloadingGnat
# @date 2022-03-18
# v 0.1.0

# Gnat Script Token
GST_INT = 'GST_INT'
GST_FLOAT = 'GST_FLOAT'
GST_PLUS = 'GST_PLUS'
GST_MINUS = 'GST_MINUS'
GST_MUL = 'GST_MUL'
GST_DIV = 'GST_DIV'
GST_LPAREN = 'GST_LPAREN'
GST_RPAREN = 'GST_RPAREN'

class Token:
    """Tokenizer for GnatScript"""
    def __init__(self, tokenType, value=None):
        self.type = tokenType
        self.value = value

    def __repr__(self):
        if self.value:
            return f'Token("{self.type}":{self.value})'
        return f'Token("{self.type}")'
    
    def __str__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'
