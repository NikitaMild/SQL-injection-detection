Grammar=MyGrammar
Lexer=$(Grammar)Lexer
Listener=$(Grammar)Listener
Parser=$(Grammar)Parser

all:	GenerateFiles main

GenerateFiles:
	antlr4 -Dlanguage=Python2 $(Grammar).g4

main: main.py
	python2 main.py

clean:
	rm -f $(Lexer).py
	rm -f $(Lexer).pyc
	rm -f $(Grammar).tokens
	rm -f $(Lexer).tokens
	rm -f $(Listener).py
	rm -f $(Listener).pyc
	rm -f $(Parser).py
	rm -f $(Parser).pyc
