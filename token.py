TT_INT = "INT"
TT_FLOAT = "FLOAT"
TT_PLUS = "PLUS"
TT_MINUS = "MINUS"
TT_MUL = "MUL"
TT_DIV = "DIV"
TT_MOD = "MOD"
TT_POW = "POW"
TT_LPAREN = "LPAREN"
TT_RPAREN="RPAREN"
NUMS = "1234567890."

class Token:
    def __init__(self, type, start, value=None,end=None):
        self.type = type
        self.value = value
        self.start = start
        self.end = end if end else start + 1

    def __repr__(self):
        return f"{self.type}{(': ' + str(self.value)) if self.value else ''}"