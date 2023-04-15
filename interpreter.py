from token import *
from value import *
class Interpreter:
    def visit(self, ast):
        return self.__getattribute__(f"visit_{type(ast).__name__}")(ast)
    
    def visit_NumberNode(self, node):
        return Number(node.token.value), None

    def visit_UnaryOperatorNode(self, node):
        if node.op.type == TT_MINUS:
            return Number(node.token.value * -1), None
        return Number(node.token.value), None

    def visit_BinaryOperatorNode(self, node):
        lft, err = self.visit(node.left)
        if err: return err
        
        op = node.op

        rt, err = self.visit(node.right)
        if err: return err
        
        if op.type == TT_PLUS:
            res, err = lft.add(rt)
            if err: return None, err
            return res, None

        if op.type == TT_MINUS:
            res, err = lft.sub(rt)
            if err: return None, err
            return res, None
        
        if op.type == TT_DIV:
            res, err = lft.div(rt)
            if err: return None, err
            return res, None

        if op.type == TT_MUL:
            res, err = lft.mul(rt)
            if err: return None, err
            return res, None

        if op.type == TT_MOD:
            res, err = lft.mod(rt)
            if err: return None, err
            return res, None

        if op.type == TT_POW:
            res, err = lft.pow(rt)
            if err: return None, err
            return res, None

            