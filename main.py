from Parser.GrammarParser import *
from CodeGenerator.Generator import *
from Semantic_Analyzer.SemanticAnalyzer import *

if __name__ == '__main__':
    # print("-" * 10, "Lexer", "-" * 10)

    lexicalAnalyzer = LexicalAnalyzer('test.cpp')
    lexicalAnalyzerResult = lexicalAnalyzer.startParsing()
    # lexicalAnalyzer.printLexemes()

    print()
    if lexicalAnalyzerResult:
        print("-" * 10, "Grammar", "-" * 10)

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

            variableStorage = VariableStorage()
            semanticAnalyser = VariableSemanticAnalyser(treeBuilder.tree)
            semanticAnalyser.parse(treeBuilder.tree, variableStorage)

            generator = Generator(treeBuilder.tree)
            generator.generate()
            print(generator.resultCode)

            # optimizer = Optimizer(treeBuilder.tree, grammarParser.rules)
            # optimizer.optimize()

    print()
