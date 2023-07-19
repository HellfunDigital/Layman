```python
import unittest
from laymen_error_handler import LaymenErrorHandler

class TestLaymenErrorHandler(unittest.TestCase):

    def setUp(self):
        self.error_handler = LaymenErrorHandler()

    def test_handle_syntax_error(self):
        with self.assertRaises(SyntaxError):
            self.error_handler.handle_error("SyntaxError", "Invalid syntax at line 1")

    def test_handle_runtime_error(self):
        with self.assertRaises(RuntimeError):
            self.error_handler.handle_error("RuntimeError", "Undefined variable at line 3")

    def test_handle_type_error(self):
        with self.assertRaises(TypeError):
            self.error_handler.handle_error("TypeError", "Invalid operation on string at line 5")

    def test_handle_name_error(self):
        with self.assertRaises(NameError):
            self.error_handler.handle_error("NameError", "Undefined function at line 7")

    def test_handle_value_error(self):
        with self.assertRaises(ValueError):
            self.error_handler.handle_error("ValueError", "Invalid value for function argument at line 9")

if __name__ == '__main__':
    unittest.main()
```