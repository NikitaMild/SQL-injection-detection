# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from antlr4 import *
from MyGrammar.MyGrammarLexer import MyGrammarLexer
from MyGrammar.MyGrammarListener import MyGrammarListener
from MyGrammar.MyGrammarParser import MyGrammarParser
from ANTLR4.ANTLR4Lexer import ANTLR4Lexer
from ANTLR4.ANTLR4Parser import ANTLR4Parser
from ANTLR4.ANTLR4ParserListener import ANTLR4ParserListener
import sys


class MyGrammarPrintListener(MyGrammarListener):
    def enterSentence(self, ctx):
        print "MyGrammar: %s" % ctx.words()[0]

    def enterWords(self, ctx):
        print "MyGrammar: %s" % ctx.FROM()

    def exitWords(self, ctx):
        print "MyGrammar: %s" % ctx.WORD()


class ANTLR4PrintListener(ANTLR4ParserListener):
    def enterRuleBlock(self, ctx):
        print "ANTLR4 ruleBlock: %s" % ctx.ruleAltList()

    def enterRuleAltList(self, ctx):
        print "ANTLR4 ruleAltList: %s" % len(ctx.labeledAlt())

    def enterLabeledAlt(self, ctx):
        print "ANTLR4 labeledAlt: %s" % ctx.labeledAlt()

    def enterAlternative(self, ctx):
        print "ANTLR4 alternative: %s" % ctx.alternative()

    def enterElement(self, ctx):
        print "ANTLR4 element: %s" % ctx.element()

    def enterAtom(self, ctx):
        print "ANTLR4 atom: %s" % ctx.atom()

    def enterTerminal(self, ctx):
        print "ANTLR4 terminal: %s" % ctx.terminal()

    def enterRuleref(self, ctx):
        print "ANTLR4 rule_ref: %s" % ctx.ruleref()


def main():
    #mygrammar_lexer = MyGrammarLexer(StdinStream())
    #mygrammar_stream = CommonTokenStream(mygrammar_lexer)
    #mygrammar_parser = MyGrammarParser(mygrammar_stream)
    #mygrammar_tree = mygrammar_parser.sentence()
    #mygrammar_printer = MyGrammarPrintListener()
    #mygrammar_walker = ParseTreeWalker()
    #mygrammar_walker.walk(mygrammar_printer, mygrammar_tree)
    #--------------------------------------------------
    ANTLR4_lexer = ANTLR4Lexer(StdinStream())
    ANTLR4_stream = CommonTokenStream(ANTLR4_lexer)
    ANTLR4_parser = ANTLR4Parser(ANTLR4_stream)
    ANTLR4_tree = ANTLR4_parser.grammarSpec()
    ANTLR4_printer = ANTLR4PrintListener()
    ANTLR4_walker = ParseTreeWalker()
    ANTLR4_walker.walk(ANTLR4_printer, ANTLR4_tree)

if __name__ == '__main__':
    main()

#2.1.1 вместо StdinStream должна пойти грамматика MyGrammar.g4
#Нужно до след. вторника:
#1. Разобраться в устрой-стве грамматики ANTLR4 для описания грамматик напримере MyGrammar
#2. Получить имя правила из RULE_REF и rule_ref и как получить значение токена (лексемы) из terminal
#3. НАписать скелет алгоритма на вход тестовая грамматика а на выходе печатается список всех нахваний правил
