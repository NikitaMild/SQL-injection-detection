# Generated from MyGrammar.g4 by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\n\n\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\b\2")
        buf.write(u"\4\3\2\2\2\4\5\7\7\2\2\5\6\7\b\2\2\6\7\7\t\2\2\7\b\7")
        buf.write(u"\n\2\2\b\3\3\2\2\2\2")
        return buf.getvalue()


class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'SELECT'", u"'*'", u"'FROM'" ]

    symbolicNames = [ u"<INVALID>", u"SPACE", u"SPEC_MYSQL_COMMENT", u"COMMENT_INPUT", 
                      u"LINE_COMMENT", u"SELECT", u"STAR", u"FROM", u"WORD" ]

    RULE_select = 0

    ruleNames =  [ u"select" ]

    EOF = Token.EOF
    SPACE=1
    SPEC_MYSQL_COMMENT=2
    COMMENT_INPUT=3
    LINE_COMMENT=4
    SELECT=5
    STAR=6
    FROM=7
    WORD=8

    def __init__(self, input):
        super(MyGrammarParser, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SelectContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MyGrammarParser.SelectContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(MyGrammarParser.SELECT, 0)

        def STAR(self):
            return self.getToken(MyGrammarParser.STAR, 0)

        def FROM(self):
            return self.getToken(MyGrammarParser.FROM, 0)

        def WORD(self):
            return self.getToken(MyGrammarParser.WORD, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_select

        def enterRule(self, listener):
            if hasattr(listener, "enterSelect"):
                listener.enterSelect(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSelect"):
                listener.exitSelect(self)




    def select(self):

        localctx = MyGrammarParser.SelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_select)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(MyGrammarParser.SELECT)
            self.state = 3
            self.match(MyGrammarParser.STAR)
            self.state = 4
            self.match(MyGrammarParser.FROM)
            self.state = 5
            self.match(MyGrammarParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





