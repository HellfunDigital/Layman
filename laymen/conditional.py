```python
class Conditional:
    def __init__(self):
        self.conditional_types = ["if", "else", "elif"]

    def is_conditional(self, token):
        return token in self.conditional_types

    def execute(self, token, condition, true_block, false_block=None):
        if token == "if":
            if condition:
                true_block.execute()
            elif false_block:
                false_block.execute()
        elif token == "else":
            if not condition:
                true_block.execute()
        elif token == "elif":
            if condition:
                true_block.execute()
            elif false_block:
                false_block.execute()
```