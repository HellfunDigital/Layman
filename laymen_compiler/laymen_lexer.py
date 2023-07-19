```python
import re

class LaymenLexer:
    def __init__(self):
        self.tokens = [
            ('KEYWORD', r'\b(?:if|then|else|for|to|do|end)\b'),
            ('ASSIGN', r'is'),
            ('OPERATOR', r'[+\-*/]'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('NUMBER', r'\d+'),
            ('ID', r'[a-zA-Z][a-zA-Z0-9_]*'),
            ('NEWLINE', r'\n'),
            ('SKIP', r'[ \t]+'),
            ('MISMATCH', r'.')
        ]

    def lex(self, code):
        pos = 0
        tokens = []
        while pos < len(code):
            match = None
            for token_expr in self.tokens:
                pattern, tag = token_expr
                regex = re.compile(pattern)
                match = regex.match(code, pos)
                if match:
                    text = match.group(0)
                    if tag:
                        token = (text, tag)
                        tokens.append(token)
                    break
            if not match:
                sys.exit(f'Illegal character: {code[pos]}')
            else:
                pos = match.end(0)
        return tokens
```