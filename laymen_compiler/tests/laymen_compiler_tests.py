```python
import unittest
from laymen_compiler import LaymenCompiler

class TestLaymenCompiler(unittest.TestCase):

    def setUp(self):
        self.compiler = LaymenCompiler()

    def test_compile(self):
        laymen_code = """
        start program
        set x to 5
        print x
        end program
        """
        expected_output = """
        int main() {
            int x = 5;
            printf("%d", x);
            return 0;
        }
        """
        self.assertEqual(self.compiler.compile(laymen_code), expected_output)

    def test_compile_with_error(self):
        laymen_code = """
        start program
        set x to 5
        print y
        end program
        """
        with self.assertRaises(Exception) as context:
            self.compiler.compile(laymen_code)
        self.assertTrue('Variable "y" is not defined' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
```