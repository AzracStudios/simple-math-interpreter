class NumberNode:
    def __init__(self, token):
        self.token = token
        self.start = self.token.start
        self.end = self.token.end
    
    def __repr__(self):
        return f"({self.token})"

class UnaryOperatorNode:
    def __init__(self, op, token):
        self.op = op
        self.token = token
        self.start = self.op.start
        self.end = self.token.end

    def __repr__(self):
        return f"({self.op} {self.token})"

class BinaryOperatorNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

        self.start = self.left.start
        self.end = self.right.end

    def __repr__(self):
        return f"({self.left} {self.op} {self.right})"