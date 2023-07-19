```python
import re
from laymen_compiler.laymen_lexer import LaymenLexer
from laymen_compiler.laymen_error_handler import LaymenErrorHandler

class LaymenParser:
    def __init__(self):
        self.lexer = LaymenLexer()
        self.error_handler = LaymenErrorHandler()

    def parse(self, laymenCode):
        tokens = self.lexer.tokenize(laymenCode)
        parsedCode = self.build_ast(tokens)
        return parsedCode

    def build_ast(self, tokens):
        ast = []
        while tokens:
            token = tokens.pop(0)
            if token.type == 'COMMAND':
                ast.append(self.parse_command(token, tokens))
            else:
                self.error_handler.throw_unexpected_token_error(token)
        return ast

    def parse_command(self, token, tokens):
        command = {'type': 'command', 'value': token.value, 'args': []}
        while tokens and tokens[0].type != 'COMMAND':
            command['args'].append(tokens.pop(0).value)
        return command
```