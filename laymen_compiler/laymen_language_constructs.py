```python
class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Loop:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

class Conditional:
    def __init__(self, condition, if_block, else_block):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

class Function:
    def __init__(self, name, parameters, block):
        self.name = name
        self.parameters = parameters
        self.block = block

class LaymenConstructs:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def create_variable(self, name, value):
        self.variables[name] = Variable(name, value)

    def create_loop(self, condition, block):
        return Loop(condition, block)

    def create_conditional(self, condition, if_block, else_block):
        return Conditional(condition, if_block, else_block)

    def create_function(self, name, parameters, block):
        self.functions[name] = Function(name, parameters, block)
```