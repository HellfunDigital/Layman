```python
class LaymenError(Exception):
    """Base class for exceptions in Laymen language."""
    pass

class SyntaxError(LaymenError):
    def __init__(self, message, line):
        self.message = message
        self.line = line

class VariableError(LaymenError):
    def __init__(self, message, variable_name):
        self.message = message
        self.variable_name = variable_name

class LoopError(LaymenError):
    def __init__(self, message, loop_type):
        self.message = message
        self.loop_type = loop_type

class ConditionalError(LaymenError):
    def __init__(self, message, condition):
        self.message = message
        self.condition = condition

class FunctionError(LaymenError):
    def __init__(self, message, function_name):
        self.message = message
        self.function_name = function_name

class LibraryIntegrationError(LaymenError):
    def __init__(self, message, library_name):
        self.message = message
        self.library_name = library_name

class APIIntegrationError(LaymenError):
    def __init__(self, message, api_name):
        self.message = message
        self.api_name = api_name

class PerformanceOptimizationError(LaymenError):
    def __init__(self, message, technique_name):
        self.message = message
        self.technique_name = technique_name
```