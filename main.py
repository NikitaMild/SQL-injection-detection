from antlr4 import *
from MyGrammarLexer import MyGrammarLexer
from MyGrammarListener import MyGrammarListener
from MyGrammarParser import MyGrammarParser
import sys


class MyGrammarPrintListener(MyGrammarListener):
    def enterSentence(self, ctx):
        print "MyGrammar: %s" % ctx.words()

    def enterWords(self, ctx):
        print "MyGrammar: %s" % ctx.FROM()

    def exitWords(self, ctx):
        print "MyGrammar: %s" % ctx.WORD()


def main():
    lexer = MyGrammarLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)
    tree = parser.sentence()
    printer = MyGrammarPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main()
