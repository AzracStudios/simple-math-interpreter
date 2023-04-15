class Error:
    def __init__(self, name, details, position):
        self.name = name
        self.details = details
        self.position = position

    def __repr__(self):
        return f"{self.name} Error{f' @ {self.position}' if self.position else ''}: {self.details}"

class IllegalCharacterError(Error):
    def __init__(self, char, pos):        
        super().__init__("Lexer", char, pos)

class UnexpectedSyntaxError(Error):
    def __init__(self, msg, pos):
        super().__init__("Parser", msg, pos)

class UnexpectedEOFError(Error):
    def __init__(self):
        super().__init__("Lexer", "Unexpected EOF", pos)

class UncaughtRuntimeError(Error):
    def __init__(self, msg, pos):
        super().__init__("Interpreter", msg, None)
