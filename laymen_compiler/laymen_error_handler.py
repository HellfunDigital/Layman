```python
class LaymenError(Exception):
    """Base class for exceptions in Laymen language."""
    pass

class SyntaxError(LaymenError):
    def __init__(self, message, line):
        self.message = message
        self.line = line

class RuntimeError(LaymenError):
    def __init__(self, message, line):
        self.message = message
        self.line = line

class ErrorHandler:
    def __init__(self):
        self.had_error = False

    def report(self, line, where, message):
        print(f"[line {line}] Error {where}: {message}")
        self.had_error = True

    def error(self, line, message):
        self.report(line, "", message)

    def runtime_error(self, error):
        print(f"{error.message}\n[line {error.line}]")
        self.had_error = True
```