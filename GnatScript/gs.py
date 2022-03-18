##
# Run
# @author UnloadingGnat
# @date 2022-03-18
# v 0.1.0

from gnatScript.lexer import Lexer


def run(filename, text):
    lexer = Lexer(filename, text)
    tokens, error = lexer.createTokens()

    return tokens, error