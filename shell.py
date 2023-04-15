from lexer import *
from parser import *
from interpreter import *

DEBUG = True
 
def shell():
    print("Math Interpreter v1.0")
    while True:
        src = input("> ")
        if src == "q":
            break
        if src.strip() == "":
            continue

        lex = Lexer(src)
        toks = lex.tokenize()

        if not toks:
            return print(UnexpectedEOFError())

        if DEBUG:
            print(f"\n==============================\nTOKENS: {toks}")
        
        par = Parser(toks)
        ast, err = par.parse()

        if err:
            return print(err)

        if DEBUG:
            print(f"ABSTRACT SYNTAX TREE: {ast}")

        intp = Interpreter()
        res, err = intp.visit(ast)

        if err:
            return print(err)

        print(("INTERPRETED RESULT: " if DEBUG else "") + str(res) + "\n==============================\n")
        


if __name__ == "__main__":
    shell()
