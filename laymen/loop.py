```python
class Loop:
    def __init__(self, loop_type, condition, block):
        self.loop_type = loop_type
        self.condition = condition
        self.block = block

    def execute(self, environment):
        if self.loop_type == "while":
            while self.condition.evaluate(environment):
                self.block.execute(environment)
        elif self.loop_type == "for":
            range_value = self.condition.evaluate(environment)
            for i in range(range_value):
                environment.set_variable("i", i)
                self.block.execute(environment)

class WhileLoop(Loop):
    def __init__(self, condition, block):
        super().__init__("while", condition, block)

class ForLoop(Loop):
    def __init__(self, condition, block):
        super().__init__("for", condition, block)
```