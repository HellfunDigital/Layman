```python
import unittest
from laymen_compiler.laymen_parser import LaymenParser
from laymen_compiler.laymen_lexer import LaymenLexer
from laymen_compiler.laymen_error_handler import LaymenErrorHandler

class TestLaymenParser(unittest.TestCase):

    def setUp(self):
        self.parser = LaymenParser()
        self.lexer = LaymenLexer()
        self.error_handler = LaymenErrorHandler()

    def test_valid_syntax(self):
        code = "create a variable named x and set it to 5"
        tokens = self.lexer.tokenize(code)
        try:
            self.parser.parse(tokens)
        except Exception as e:
            self.fail(f"Valid syntax raised an exception: {e}")

    def test_invalid_syntax(self):
        code = "create a variable named and set it to 5"
        tokens = self.lexer.tokenize(code)
        with self.assertRaises(Exception):
            self.parser.parse(tokens)

    def test_error_handling(self):
        code = "create a variable named and set it to 5"
        tokens = self.lexer.tokenize(code)
        try:
            self.parser.parse(tokens)
        except Exception as e:
            self.assertEqual(str(e), self.error_handler.handle_syntax_error(tokens))

if __name__ == '__main__':
    unittest.main()
```