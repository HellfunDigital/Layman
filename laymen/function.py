```python
class Function:
    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters
        self.body = body

    def execute(self, args):
        if len(args) != len(self.parameters):
            raise Exception(f"Function '{self.name}' expected {len(self.parameters)} arguments, got {len(args)}")

        # Create a new scope for function execution
        scope = {}

        # Assign arguments to parameters in the new scope
        for i in range(len(args)):
            scope[self.parameters[i]] = args[i]

        # Execute the function body
        for statement in self.body:
            result = statement.execute(scope)
            if result is not None:
                return result

    def __str__(self):
        return f"Function '{self.name}' with parameters {self.parameters}"

class FunctionDeclaration:
    def __init__(self, function):
        self.function = function

    def execute(self, scope):
        scope[self.function.name] = self.function

class FunctionCall:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

    def execute(self, scope):
        if self.name not in scope:
            raise Exception(f"Function '{self.name}' is not defined")

        function = scope[self.name]

        if not isinstance(function, Function):
            raise Exception(f"'{self.name}' is not a function")

        args = [arg.execute(scope) for arg in self.arguments]

        return function.execute(args)
```