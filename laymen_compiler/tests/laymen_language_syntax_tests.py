```python
import unittest
from laymen_compiler import laymen_language_syntax

class TestLaymenLanguageSyntax(unittest.TestCase):

    def setUp(self):
        self.syntax = laymen_language_syntax.LaymenLanguageSyntax()

    def test_valid_syntax(self):
        code = "start with x equal to 5"
        self.assertTrue(self.syntax.is_valid(code))

    def test_invalid_syntax(self):
        code = "start x equal to 5"
        self.assertFalse(self.syntax.is_valid(code))

    def test_variable_declaration(self):
        code = "start with x equal to 5"
        self.assertEqual(self.syntax.parse(code), {"type": "declaration", "name": "x", "value": 5})

    def test_conditional_statement(self):
        code = "if x is greater than 5 then display 'x is big'"
        self.assertEqual(self.syntax.parse(code), {"type": "conditional", "condition": {"type": "comparison", "left": "x", "operator": ">", "right": 5}, "then": {"type": "display", "message": "x is big"}})

    def test_loop_statement(self):
        code = "repeat 5 times display 'Hello'"
        self.assertEqual(self.syntax.parse(code), {"type": "loop", "times": 5, "action": {"type": "display", "message": "Hello"}})

if __name__ == '__main__':
    unittest.main()
```