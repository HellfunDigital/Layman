```python
import unittest
from laymen_compiler.laymen_lexer import LaymenLexer

class TestLaymenLexer(unittest.TestCase):

    def setUp(self):
        self.lexer = LaymenLexer()

    def test_tokenize(self):
        code = "create variable x as 10"
        tokens = self.lexer.tokenize(code)
        self.assertEqual(len(tokens), 5)
        self.assertEqual(tokens[0].type, 'CREATE')
        self.assertEqual(tokens[1].type, 'VARIABLE')
        self.assertEqual(tokens[2].type, 'IDENTIFIER')
        self.assertEqual(tokens[3].type, 'AS')
        self.assertEqual(tokens[4].type, 'NUMBER')

    def test_invalid_token(self):
        code = "create variable x as &"
        with self.assertRaises(Exception) as context:
            self.lexer.tokenize(code)
        self.assertTrue('Invalid character' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
```