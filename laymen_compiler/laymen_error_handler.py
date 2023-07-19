```python
class LaymenErrorHandler:
    def __init__(self):
        self.debugInfo = []

    def add_error(self, error):
        self.debugInfo.append(error)

    def clear_errors(self):
        self.debugInfo = []

    def get_errors(self):
        return self.debugInfo

    def has_errors(self):
        return len(self.debugInfo) > 0

    def print_errors(self):
        for error in self.debugInfo:
            print(f"Error: {error}")

    def handle_error(self, error):
        self.add_error(error)
        self.print_errors()
```