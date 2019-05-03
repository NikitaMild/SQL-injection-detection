gram=?
MyLexer=$(gram)Lexer
MyListener=$(gram)Listener
MyParser=$(gram)Parser
path_to_dir=/home/cucumber/kursuch/4/litegramm/$(gram)/

mygrammar: create1 move1

antlr4: create2 move2

create1: $(gram)
	antlr4 -Dlanguage=Python2 $(gram).g4

create2: $(gram)
	antlr4 -Dlanguage=Python2 $(gram)Lexer.g4
	antlr4 -Dlanguage=Python2 $(gram)Parser.g4

main: main.py
	python2 main.py

move1:
	@(mv $(MyLexer).py $(gram).tokens $(MyLexer).tokens $(path_to_dir))
	@(mv $(MyListener).py $(MyParser).py $(path_to_dir))

move2:
	@(mv $(MyLexer).py $(MyLexer).tokens $(MyParser).py $(MyParser).tokens $(MyParser)Listener.py $(path_to_dir))

clean:
	rm -f $(path_to_dir)$(MyLexer).py
	rm -f $(path_to_dir)$(MyLexer).pyc
	rm -f $(path_to_dir)$(gram).tokens
	rm -f $(path_to_dir)$(MyLexer).tokens
	rm -f $(path_to_dir)$(MyListener).py
	rm -f $(path_to_dir)$(MyListener).pyc
	rm -f $(path_to_dir)$(MyParser).py
	rm -f $(path_to_dir)$(MyParser).pyc
	rm -f $(path_to_dir)$(MyParser).tokens
	rm -f $(path_to_dir)$(MyParser)Listener.py
	rm -f $(path_to_dir)$(MyParser)Listener.pyc
	rm -f $(path_to_dir)__init__.pyc
