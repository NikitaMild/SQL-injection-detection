from MyGrammarListener import MyGrammarListener


class NewMyGrammarListener (MyGrammarListener):
    def enterSelect(self, ctx):
        print("Enter")

    def exitSelect(self, ctx):
        print("Exit")
