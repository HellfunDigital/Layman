```python
import unittest
from laymen_compiler import laymen_debugger

class TestLaymenDebugger(unittest.TestCase):

    def setUp(self):
        self.debugger = laymen_debugger.LaymenDebugger()

    def test_breakpoint(self):
        code = "start program\nset x to 5\nend program"
        self.debugger.set_breakpoint(2)
        self.debugger.run(code)
        self.assertEqual(self.debugger.current_line, 2)

    def test_step_over(self):
        code = "start program\nset x to 5\nset y to 10\nend program"
        self.debugger.run(code)
        self.debugger.step_over()
        self.assertEqual(self.debugger.current_line, 3)

    def test_step_into(self):
        code = "start program\nfunction add x y\nreturn x plus y\nend function\nset z to add 5 10\nend program"
        self.debugger.run(code)
        self.debugger.step_into()
        self.assertEqual(self.debugger.current_line, 2)

    def test_watch_variable(self):
        code = "start program\nset x to 5\nset x to 10\nend program"
        self.debugger.run(code)
        self.debugger.watch_variable('x')
        self.assertEqual(self.debugger.watched_variables['x'], 10)

if __name__ == '__main__':
    unittest.main()
```