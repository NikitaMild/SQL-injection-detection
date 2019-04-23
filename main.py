# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from antlr4 import *
from MyGrammar.MyGrammarLexer import MyGrammarLexer
from MyGrammar.MyGrammarListener import MyGrammarListener
from MyGrammar.MyGrammarParser import MyGrammarParser
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

#2.1.1 вместо StdinStream должна пойти грамматика MyGrammar.g4
#Нужно до след. вторника:
#1. Разобраться в устрой-стве грамматики ANTLR4 для описания грамматик напримере MyGrammar
#2. Получить имя правила из RULE_REF и rule_ref и как получить значение токена (лексемы) из terminal
#3. НАписать скелет алгоритма на вход тестовая грамматика а на выходе печатается список всех нахваний правил
