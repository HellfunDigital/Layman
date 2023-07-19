```python
class Debugger:
    def __init__(self):
        self.breakpoints = []
        self.current_line = 0

    def set_breakpoint(self, line_number):
        if line_number not in self.breakpoints:
            self.breakpoints.append(line_number)

    def remove_breakpoint(self, line_number):
        if line_number in self.breakpoints:
            self.breakpoints.remove(line_number)

    def clear_breakpoints(self):
        self.breakpoints = []

    def step_into(self):
        self.current_line += 1

    def step_over(self, block_end_line):
        self.current_line = block_end_line + 1

    def continue_execution(self):
        self.current_line = max(self.breakpoints)

    def print_debug_info(self, variables, call_stack):
        print(f"Current Line: {self.current_line}")
        print("Variables:")
        for var_name, var_value in variables.items():
            print(f"  {var_name} = {var_value}")
        print("Call Stack:")
        for function_name in call_stack:
            print(f"  {function_name}")

    def handle_breakpoint(self, line_number, variables, call_stack):
        if line_number in self.breakpoints:
            print(f"Breakpoint at line {line_number}")
            self.print_debug_info(variables, call_stack)
            return True
        return False
```