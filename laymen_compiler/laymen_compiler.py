```python
from laymen_parser import parseLaymenCode
from laymen_lexer import lexLaymenCode
from laymen_interpreter import interpretLaymenCode
from laymen_error_handler import handleLaymenError

class LaymenCompiler:
    def __init__(self):
        self.laymenCode = ""
        self.parsedCode = None
        self.compiledCode = None

    def compileLaymenCode(self, laymenCode):
        self.laymenCode = laymenCode
        try:
            lexedCode = lexLaymenCode(self.laymenCode)
            self.parsedCode = parseLaymenCode(lexedCode)
            self.compiledCode = interpretLaymenCode(self.parsedCode)
            return self.compiledCode
        except Exception as e:
            handleLaymenError(e)

    def getCompiledCode(self):
        return self.compiledCode

    def getParsedCode(self):
        return self.parsedCode
```