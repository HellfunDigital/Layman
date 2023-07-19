```python
import sys
from laymen.lexer import Lexer
from laymen.parser import Parser
from laymen.compiler import Compiler
from laymen.error_handling import ErrorHandler
from laymen.debugger import Debugger
from laymen.visual_interface import VisualInterface
from laymen.documentation import Documentation
from laymen.tutorial import Tutorial
from laymen.community import Community
from laymen.feedback import Feedback

class Laymen:
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()
        self.compiler = Compiler()
        self.error_handler = ErrorHandler()
        self.debugger = Debugger()
        self.visual_interface = VisualInterface()
        self.documentation = Documentation()
        self.tutorial = Tutorial()
        self.community = Community()
        self.feedback = Feedback()

    def run(self, source_code):
        tokens = self.lexer.tokenize(source_code)
        ast = self.parser.parse(tokens)
        self.compiler.compile(ast)

    def handle_error(self, error):
        self.error_handler.handle(error)

    def debug(self, source_code):
        tokens = self.lexer.tokenize(source_code)
        ast = self.parser.parse(tokens)
        self.debugger.debug(ast)

    def show_visual_interface(self):
        self.visual_interface.show()

    def show_documentation(self):
        self.documentation.show()

    def show_tutorial(self):
        self.tutorial.show()

    def join_community(self):
        self.community.join()

    def give_feedback(self, feedback):
        self.feedback.give(feedback)

if __name__ == "__main__":
    laymen = Laymen()

    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            source_code = file.read()
            laymen.run(source_code)
    else:
        laymen.show_visual_interface()
```