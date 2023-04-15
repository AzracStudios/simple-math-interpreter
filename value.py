class Number:
    def __init__(self, val):
        self.val = val
    
    def add(self, other):
        return Number(self.val + other.val), None

    def sub(self, other):
        return Number(self.val - other.val), None

    def mul(self, other):
        return Number(self.val * other.val), None

    def pow(self, other):
        return Number(self.val ** other.val), None

    def div(self, other):
        if other.val == 0:
            return None, UncaughtRuntimeError("Division by 0")
        return Number(self.val / other.val), None
    
    def mod(self, other):
        if other.val == 0:
            return None, UncaughtRuntimeError("Division by 0")
        return Number(self.val % other.val), None
    
    def __repr__(self):
        return f"{self.val}"