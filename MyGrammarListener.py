# Generated from MyGrammar.g4 by ANTLR 4.5.1
from antlr4 import *

# This class defines a complete listener
# for a parse tree produced by MyGrammarParser.


class MyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammarParser#select.
    def enterSelect(self, ctx):
        pass

    # Exit a parse tree produced by MyGrammarParser#select.
    def exitSelect(self, ctx):
        pass


class NewMyGrammarListener (MyGrammarListener):
    def enterSelect(self, ctx):
        print("Enter")

    def exitSelect(self, ctx):
        print("Exit")
