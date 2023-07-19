```python
import unittest
from laymen_compiler import laymen_language_constructs

class TestLaymenLanguageConstructs(unittest.TestCase):

    def setUp(self):
        self.constructs = laymen_language_constructs.LaymenLanguageConstructs()

    def test_variable_declaration(self):
        code = "Create a variable named 'x' with value 10."
        result = self.constructs.parse(code)
        self.assertEqual(result, {'type': 'variable_declaration', 'name': 'x', 'value': 10})

    def test_loop_structure(self):
        code = "Repeat 5 times: print 'Hello, World!'"
        result = self.constructs.parse(code)
        self.assertEqual(result, {'type': 'loop', 'times': 5, 'body': "print 'Hello, World!'"})

    def test_conditional_structure(self):
        code = "If 'x' is greater than 5, print 'x is big.'"
        result = self.constructs.parse(code)
        self.assertEqual(result, {'type': 'conditional', 'condition': "x > 5", 'body': "print 'x is big.'"})

    def test_function_declaration(self):
        code = "Define a function named 'greet' that takes 'name' as parameter and prints 'Hello, ' followed by 'name'."
        result = self.constructs.parse(code)
        self.assertEqual(result, {'type': 'function_declaration', 'name': 'greet', 'parameters': ['name'], 'body': "print 'Hello, ' + name"})

if __name__ == '__main__':
    unittest.main()
```