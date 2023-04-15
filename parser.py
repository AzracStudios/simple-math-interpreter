from token import *
from nodes import *
from error import *


class Parser:
    def __init__(self, toks):
        self.toks = toks
        self.cur_tok = None
        self.idx = -1
        self.advance()

    def advance(self):
        self.idx += 1
        self.cur_tok = None

        if self.idx < len(self.toks):
            self.cur_tok = self.toks[self.idx]

    def parse(self):
        return self.expr()

    def factor(self):
        tok = self.cur_tok

        if tok.type in (TT_INT, TT_FLOAT):
            self.advance()
            return NumberNode(tok), None
        
        if tok.type in (TT_PLUS, TT_MINUS):
            self.advance()

            if self.cur_tok.type in (TT_INT, TT_FLOAT):
                return UnaryOperatorNode(tok, self.cur_tok), None
            
            return None, UnexpectedSyntaxError("Expected int or float", self.idx)

        if tok.type == TT_LPAREN:
            self.advance()

            expr, err = self.expr()
            
            if err:
                return None, err
            
            if self.cur_tok.type != TT_RPAREN:
                return None, UnexpectedSyntaxError("Expected ')'", self.idx)

            self.advance()

            return expr, None


    def term(self):
        return self.make_binary_operator_node(self.factor, (TT_MUL, TT_DIV))

    def expr(self):
        return self.make_binary_operator_node(self.term, (TT_PLUS, TT_MINUS))

    def make_binary_operator_node(self, func, ops):

        left, err = func()
        if err:
            return None, err

        while self.cur_tok:
            if self.cur_tok.type in ops:
                op = self.cur_tok
                self.advance()

                right, err = func()
                if err:
                    return None, err
                
                left = BinaryOperatorNode(left, op, right)
            else:
                break
        return (left, None)