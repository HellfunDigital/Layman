```python
import re
from laymen.token import Token, TokenType

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_char = ''
        self.next_char = ''

    def tokenize(self):
        self.source_code = self.source_code.split()

        for word in self.source_code:
            if word == "start":
                self.tokens.append(Token(TokenType.START))
            elif word == "end":
                self.tokens.append(Token(TokenType.END))
            elif word == "if":
                self.tokens.append(Token(TokenType.IF))
            elif word == "else":
                self.tokens.append(Token(TokenType.ELSE))
            elif word == "repeat":
                self.tokens.append(Token(TokenType.REPEAT))
            elif word == "times":
                self.tokens.append(Token(TokenType.TIMES))
            elif word == "show":
                self.tokens.append(Token(TokenType.SHOW))
            elif word == "input":
                self.tokens.append(Token(TokenType.INPUT))
            elif word == "set":
                self.tokens.append(Token(TokenType.SET))
            elif word == "to":
                self.tokens.append(Token(TokenType.TO))
            elif re.match("[0-9]+", word):
                self.tokens.append(Token(TokenType.NUMBER, int(word)))
            elif re.match("[a-zA-Z_][a-zA-Z0-9_]*", word):
                self.tokens.append(Token(TokenType.IDENTIFIER, word))
            else:
                self.tokens.append(Token(TokenType.UNKNOWN, word))

        return self.tokens
```