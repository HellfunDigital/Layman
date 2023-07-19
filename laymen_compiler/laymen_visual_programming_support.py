```python
import tkinter as tk
from laymen_compiler.laymen_lexer import LaymenLexer
from laymen_compiler.laymen_parser import LaymenParser
from laymen_compiler.laymen_interpreter import LaymenInterpreter
from laymen_compiler.laymen_error_handler import LaymenErrorHandler

class LaymenVisualProgrammingSupport:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Laymen Visual Programming")
        self.lexer = LaymenLexer()
        self.parser = LaymenParser()
        self.interpreter = LaymenInterpreter()
        self.error_handler = LaymenErrorHandler()

    def create_visual_block(self, block_type, block_text):
        block = tk.Button(self.root, text=block_text)
        block.pack()
        block.bind("<Button-1>", self.execute_block(block_type, block_text))

    def execute_block(self, block_type, block_text):
        def _execute(event):
            try:
                tokens = self.lexer.tokenize(block_text)
                tree = self.parser.parse(tokens)
                self.interpreter.interpret(tree)
            except Exception as e:
                self.error_handler.handle(e)
        return _execute

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    visual_programming_support = LaymenVisualProgrammingSupport()
    visual_programming_support.create_visual_block("print", "Print Hello World")
    visual_programming_support.run()
```