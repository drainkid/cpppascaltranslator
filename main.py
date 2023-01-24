from Lexer.LexicalAnalyzer import *
from Parser.GrammarParser import *
from CodeGenerator.Generator import *
from Semantic_Analyzer.SemanticAnalyzer import *



#     # print("-" * 10, "Lexer", "-" * 10)

lexicalAnalyzer = LexicalAnalyzer('test.cpp')
lexicalAnalyzerResult = lexicalAnalyzer.startParsing()
# lexicalAnalyzer.printLexemes()

print()
if lexicalAnalyzerResult:
    # print("-"*10, "Grammar", "-"*10)

    grammarParser = GrammarParser()
    grammarParser.parseJsonRules('grammar.json')
    # grammarParser.printRules()

    earley = Earley(grammarParser.rules, "<программа>")

    earleyParseResult = earley.parse(lexicalAnalyzer.lexemeArray)
    earley.printTableToFile()
    earley.printError()
    earleyTable = earley.table

    # exit(-1)

    if earleyParseResult:
        treeBuilder = TreeBuilder(earleyTable, grammarParser.rules)
        treeBuilder.buildTree()
        treeBuilder.printTreeToFile()

        generator = Generator(treeBuilder.tree)
        generator.generate()
        print(generator.resultCode)

        variableStorage = VariableStorage()
        semanticAnalyser = VariableSemanticAnalyser(treeBuilder.tree)
        semanticAnalyser.parse(treeBuilder.tree, variableStorage)

    print()