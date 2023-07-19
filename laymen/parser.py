```python
from laymen.lexer import Lexer
from laymen.token import TokenType
from laymen.syntax_tree import SyntaxTree
from laymen.variable import Variable
from laymen.loop import Loop
from laymen.conditional import Conditional
from laymen.function import Function
from laymen.error_handling import ParserError

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, message):
        raise ParserError(message)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Expected token {token_type}, but got {self.current_token.type}")

    def parse(self):
        return self.program()

    def program(self):
        nodes = self.statement_list()
        return SyntaxTree(nodes)

    def statement_list(self):
        node = self.statement()
        nodes = [node]

        while self.current_token.type == TokenType.SEMI:
            self.eat(TokenType.SEMI)
            nodes.append(self.statement())

        if self.current_token.type != TokenType.EOF:
            self.error("Expected end of file")

        return nodes

    def statement(self):
        if self.current_token.type == TokenType.VARIABLE:
            node = self.variable_declaration()
        elif self.current_token.type == TokenType.LOOP:
            node = self.loop_declaration()
        elif self.current_token.type == TokenType.CONDITIONAL:
            node = self.conditional_declaration()
        elif self.current_token.type == TokenType.FUNCTION:
            node = self.function_declaration()
        else:
            self.error("Invalid statement")

        return node

    def variable_declaration(self):
        self.eat(TokenType.VARIABLE)
        var_name = self.current_token.value
        self.eat(TokenType.ID)
        self.eat(TokenType.EQUALS)
        var_value = self.current_token.value
        self.eat(TokenType.ID)
        return Variable(var_name, var_value)

    def loop_declaration(self):
        self.eat(TokenType.LOOP)
        loop_type = self.current_token.value
        self.eat(TokenType.ID)
        loop_body = self.statement_list()
        self.eat(TokenType.END)
        return Loop(loop_type, loop_body)

    def conditional_declaration(self):
        self.eat(TokenType.CONDITIONAL)
        condition = self.current_token.value
        self.eat(TokenType.ID)
        conditional_body = self.statement_list()
        self.eat(TokenType.END)
        return Conditional(condition, conditional_body)

    def function_declaration(self):
        self.eat(TokenType.FUNCTION)
        function_name = self.current_token.value
        self.eat(TokenType.ID)
        function_body = self.statement_list()
        self.eat(TokenType.END)
        return Function(function_name, function_body)
```