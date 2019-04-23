# Generated from MyGrammar.g4 by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\13\24\4\2\t\2\4\3\t\3\3\2\7\2\b\n\2\f\2\16\2\13\13\2")
        buf.write(u"\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\2\2\4\2\4\2\2\22\2\t")
        buf.write(u"\3\2\2\2\4\16\3\2\2\2\6\b\5\4\3\2\7\6\3\2\2\2\b\13\3")
        buf.write(u"\2\2\2\t\7\3\2\2\2\t\n\3\2\2\2\n\f\3\2\2\2\13\t\3\2\2")
        buf.write(u"\2\f\r\7\2\2\3\r\3\3\2\2\2\16\17\7\4\2\2\17\20\7\5\2")
        buf.write(u"\2\20\21\7\6\2\2\21\22\7\t\2\2\22\5\3\2\2\2\3\t")
        return buf.getvalue()


class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"'SELECT'", u"'*'", u"'FROM'", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"';'" ]

    symbolicNames = [ u"<INVALID>", u"WS", u"SELECT", u"STAR", u"FROM", 
                      u"LOWERCASE", u"UPPERCASE", u"WORD", u"END", u"STRING" ]

    RULE_sentence = 0
    RULE_words = 1

    ruleNames =  [ u"sentence", u"words" ]

    EOF = Token.EOF
    WS=1
    SELECT=2
    STAR=3
    FROM=4
    LOWERCASE=5
    UPPERCASE=6
    WORD=7
    END=8
    STRING=9

    def __init__(self, input):
        super(MyGrammarParser, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SentenceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MyGrammarParser.SentenceContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MyGrammarParser.EOF, 0)

        def words(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.WordsContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.WordsContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_sentence

        def enterRule(self, listener):
            if hasattr(listener, "enterSentence"):
                listener.enterSentence(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSentence"):
                listener.exitSentence(self)




    def sentence(self):

        localctx = MyGrammarParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MyGrammarParser.SELECT:
                self.state = 4
                self.words()
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 10
            self.match(MyGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WordsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MyGrammarParser.WordsContext, self).__init__(parent, invokingState)
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
            return MyGrammarParser.RULE_words

        def enterRule(self, listener):
            if hasattr(listener, "enterWords"):
                listener.enterWords(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWords"):
                listener.exitWords(self)




    def words(self):

        localctx = MyGrammarParser.WordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_words)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(MyGrammarParser.SELECT)
            self.state = 13
            self.match(MyGrammarParser.STAR)
            self.state = 14
            self.match(MyGrammarParser.FROM)
            self.state = 15
            self.match(MyGrammarParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





