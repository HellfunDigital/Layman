```python
import laymen_lexer
import laymen_error_handler

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = 0
        self.error_handler = laymen_error_handler.ErrorHandler()

    def parse(self):
        while self.token_index < len(self.tokens):
            token_type = self.tokens[self.token_index].type

            if token_type == 'VAR_DECLARATION':
                self.parse_variable_declaration(self.tokens[self.token_index:])
            elif token_type == 'LOOP':
                self.parse_loop(self.tokens[self.token_index:])
            elif token_type == 'IF':
                self.parse_if_statement(self.tokens[self.token_index:])
            elif token_type == 'FUNCTION':
                self.parse_function(self.tokens[self.token_index:])
            else:
                self.error_handler.report_error("Unexpected token type: " + token_type)

            self.token_index += 1

    def parse_variable_declaration(self, tokens):
        # Parse variable declaration here
        pass

    def parse_loop(self, tokens):
        # Parse loop here
        pass

    def parse_if_statement(self, tokens):
        # Parse if statement here
        pass

    def parse_function(self, tokens):
        # Parse function here
        pass

if __name__ == "__main__":
    lexer = laymen_lexer.Lexer("test.laymen")
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    parser.parse()
```