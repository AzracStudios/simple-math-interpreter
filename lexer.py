from token import *
from error import *
class Lexer:
    def __init__(self, src):
        self.src = src
        self.idx = -1
        self.char = None
        self.should_advance_next_ittr = True
        self.tokens = []
        self.advance()

    def advance(self):
        self.idx += 1
        self.char = None
        if self.idx < len(self.src):
            self.char = self.src[self.idx]

    def next(self):
        if self.char == " ":
            return False, None

        if self.char == "+":
            return Token(TT_PLUS, self.idx), None

        if self.char == "-":
            return Token(TT_MINUS, self.idx), None

        if self.char == "*":
            return Token(TT_MUL, self.idx), None

        if self.char == "/":
            return Token(TT_DIV, self.idx), None

        if self.char == "%":
            return Token(TT_MOD, self.idx), None

        if self.char == "^":
            return Token(TT_POW, self.idx), None

        if self.char == "(":
            return Token(TT_LPAREN, self.idx), None
        
        if self.char == ")":
            return Token(TT_RPAREN, self.idx), None

        if self.char in NUMS:
            numstr = ""
            start = self.idx
            is_float = False

            while self.char != None:
                if self.char in NUMS:
                    if self.char == ".":
                        if is_float:
                            return None, IllegalCharacterError(self.char, self.idx)

                        is_float = True
                

                    numstr += self.char
                    self.advance()
                else:
                    break

            t = TT_FLOAT if is_float else TT_INT
            v = float(numstr) if is_float else int(numstr)
            self.should_advance_next_ittr = False
            return Token(t, start, value=v, end=start + 1), None

        return None, IllegalCharacterError(self.char, self.idx)


    def tokenize(self):
        while self.char != None:
            next, err = self.next()
            
            if err:
                return print(err)

            if next:
                self.tokens.append(next)

            if self.should_advance_next_ittr:
                self.advance()
            
            if not self.should_advance_next_ittr:
                self.should_advance_next_ittr = True

        return self.tokens