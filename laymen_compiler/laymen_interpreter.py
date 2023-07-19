```python
import laymen_lexer
import laymen_parser
import laymen_error_handler

class LaymenInterpreter:
    def __init__(self):
        self.lexer = laymen_lexer.LaymenLexer()
        self.parser = laymen_parser.LaymenParser()
        self.error_handler = laymen_error_handler.LaymenErrorHandler()

    def interpret(self, code):
        tokens = self.lexer.tokenize(code)
        if self.error_handler.has_errors():
            self.error_handler.print_errors()
            return

        parse_tree = self.parser.parse(tokens)
        if self.error_handler.has_errors():
            self.error_handler.print_errors()
            return

        self.execute(parse_tree)

    def execute(self, parse_tree):
        for node in parse_tree:
            if node.type == 'assignment':
                self.variables[node.name] = self.evaluate(node.value)
            elif node.type == 'print':
                print(self.evaluate(node.value))
            else:
                self.error_handler.report_error(f"Unknown node type: {node.type}")

    def evaluate(self, node):
        if node.type == 'number':
            return node.value
        elif node.type == 'variable':
            return self.variables[node.name]
        elif node.type == 'binary_operation':
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            if node.operator == '+':
                return left + right
            elif node.operator == '-':
                return left - right
            elif node.operator == '*':
                return left * right
            elif node.operator == '/':
                return left / right
            else:
                self.error_handler.report_error(f"Unknown operator: {node.operator}")
        else:
            self.error_handler.report_error(f"Unknown node type: {node.type}")

if __name__ == "__main__":
    interpreter = LaymenInterpreter()
    while True:
        try:
            code = input("Laymen> ")
            interpreter.interpret(code)
        except EOFError:
            break
```