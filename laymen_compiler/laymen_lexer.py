```python
import re

class LaymenLexer:
    def __init__(self):
        self.tokens = []
        self.current_char = None
        self.next_char = None
        self.source_code = None

    def load_code(self, source_code):
        self.source_code = source_code
        self.current_char = self.source_code[0]
        if len(self.source_code) > 1:
            self.next_char = self.source_code[1]
        else:
            self.next_char = None

    def advance(self):
        self.current_char = self.next_char
        if self.next_char is not None and len(self.source_code) > 1:
            self.source_code = self.source_code[1:]
            if len(self.source_code) > 1:
                self.next_char = self.source_code[1]
            else:
                self.next_char = None
        else:
            self.next_char = None

    def tokenize(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
            elif self.current_char.isdigit():
                self.tokenize_number()
            elif self.current_char.isalpha():
                self.tokenize_identifier()
            elif self.current_char == '"':
                self.tokenize_string()
            elif self.current_char == '+':
                self.tokens.append(('PLUS', '+'))
                self.advance()
            elif self.current_char == '-':
                self.tokens.append(('MINUS', '-'))
                self.advance()
            elif self.current_char == '*':
                self.tokens.append(('MULTIPLY', '*'))
                self.advance()
            elif self.current_char == '/':
                self.tokens.append(('DIVIDE', '/'))
                self.advance()
            elif self.current_char == '(':
                self.tokens.append(('LPAREN', '('))
                self.advance()
            elif self.current_char == ')':
                self.tokens.append(('RPAREN', ')'))
                self.advance()
            else:
                raise Exception(f'Unexpected character: {self.current_char}')

    def tokenize_number(self):
        number = self.current_char
        while self.next_char is not None and self.next_char.isdigit():
            number += self.next_char
            self.advance()
        if self.next_char == '.':
            number += self.next_char
            self.advance()
            while self.next_char is not None and self.next_char.isdigit():
                number += self.next_char
                self.advance()
            self.tokens.append(('FLOAT', float(number)))
        else:
            self.tokens.append(('INTEGER', int(number)))
        self.advance()

    def tokenize_identifier(self):
        identifier = self.current_char
        while self.next_char is not None and self.next_char.isalnum():
            identifier += self.next_char
            self.advance()
        self.tokens.append(('IDENTIFIER', identifier))
        self.advance()

    def tokenize_string(self):
        string = ''
        self.advance()
        while self.current_char != '"':
            string += self.current_char
            self.advance()
        self.tokens.append(('STRING', string))
        self.advance()
```