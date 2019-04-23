# Generated from MyGrammar.g4 by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\13?\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\6\2\27\n\2\r\2\16\2")
        buf.write(u"\30\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3")
        buf.write(u"\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\6\b\61\n\b\r\b")
        buf.write(u"\16\b\62\3\t\3\t\3\n\3\n\7\n9\n\n\f\n\16\n<\13\n\3\n")
        buf.write(u"\3\n\2\2\13\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write(u"\3\2\6\5\2\13\f\17\17\"\"\3\2c|\3\2C\\\4\2$$``B\2\3\3")
        buf.write(u"\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write(u"\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write(u"\3\26\3\2\2\2\5\34\3\2\2\2\7#\3\2\2\2\t%\3\2\2\2\13*")
        buf.write(u"\3\2\2\2\r,\3\2\2\2\17\60\3\2\2\2\21\64\3\2\2\2\23\66")
        buf.write(u"\3\2\2\2\25\27\t\2\2\2\26\25\3\2\2\2\27\30\3\2\2\2\30")
        buf.write(u"\26\3\2\2\2\30\31\3\2\2\2\31\32\3\2\2\2\32\33\b\2\2\2")
        buf.write(u"\33\4\3\2\2\2\34\35\7U\2\2\35\36\7G\2\2\36\37\7N\2\2")
        buf.write(u"\37 \7G\2\2 !\7E\2\2!\"\7V\2\2\"\6\3\2\2\2#$\7,\2\2$")
        buf.write(u"\b\3\2\2\2%&\7H\2\2&\'\7T\2\2\'(\7Q\2\2()\7O\2\2)\n\3")
        buf.write(u"\2\2\2*+\t\3\2\2+\f\3\2\2\2,-\t\4\2\2-\16\3\2\2\2.\61")
        buf.write(u"\5\13\6\2/\61\5\r\7\2\60.\3\2\2\2\60/\3\2\2\2\61\62\3")
        buf.write(u"\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\20\3\2\2\2\64\65")
        buf.write(u"\7=\2\2\65\22\3\2\2\2\66:\7$\2\2\679\t\5\2\28\67\3\2")
        buf.write(u"\2\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2;=\3\2\2\2<:\3\2\2")
        buf.write(u"\2=>\7$\2\2>\24\3\2\2\2\7\2\30\60\62:\3\b\2\2")
        return buf.getvalue()


class MyGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    WS = 1
    SELECT = 2
    STAR = 3
    FROM = 4
    LOWERCASE = 5
    UPPERCASE = 6
    WORD = 7
    END = 8
    STRING = 9

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'SELECT'", u"'*'", u"'FROM'", u"';'" ]

    symbolicNames = [ u"<INVALID>",
            u"WS", u"SELECT", u"STAR", u"FROM", u"LOWERCASE", u"UPPERCASE", 
            u"WORD", u"END", u"STRING" ]

    ruleNames = [ u"WS", u"SELECT", u"STAR", u"FROM", u"LOWERCASE", u"UPPERCASE", 
                  u"WORD", u"END", u"STRING" ]

    grammarFileName = u"MyGrammar.g4"

    def __init__(self, input=None):
        super(MyGrammarLexer, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


