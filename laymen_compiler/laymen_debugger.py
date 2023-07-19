```python
import laymen_lexer
import laymen_parser
import laymen_error_handler

class LaymenDebugger:
    def __init__(self):
        self.lexer = laymen_lexer.LaymenLexer()
        self.parser = laymen_parser.LaymenParser()
        self.error_handler = laymen_error_handler.LaymenErrorHandler()

    def debug(self, code):
        tokens, error = self.lexer.make_tokens(code)
        if error: 
            return None, error

        ast, error = self.parser.parse(tokens)
        if error: 
            return None, error

        return ast, None

    def step_through(self, code):
        tokens, error = self.lexer.make_tokens(code)
        if error: 
            return None, error

        ast, error = self.parser.parse(tokens)
        if error: 
            return None, error

        for node in ast.nodes:
            print(f"Stepping into: {node}")
            result, error = node.execute()
            if error:
                self.error_handler.handle(error)
                break

            print(f"Result: {result}")

if __name__ == "__main__":
    debugger = LaymenDebugger()
    while True:
        code = input("Laymen > ")
        if code.strip() == "QUIT": break
        debugger.step_through(code)
```