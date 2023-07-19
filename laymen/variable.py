```python
class Variable:
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

# Variable Types
INTEGER = "INTEGER"
FLOAT = "FLOAT"
STRING = "STRING"
BOOLEAN = "BOOLEAN"
LIST = "LIST"
DICTIONARY = "DICTIONARY"

# Example usage:
# my_var = Variable("my_var", 10, INTEGER)
# print(my_var.get_value())  # Output: 10
# my_var.set_value(20)
# print(my_var.get_value())  # Output: 20
```