```python
import unittest
from laymen_compiler import laymen_optimizer

class TestLaymenOptimizer(unittest.TestCase):

    def setUp(self):
        self.optimizer = laymen_optimizer.LaymenOptimizer()

    def test_optimize(self):
        code = """
        start program
        set x to 5
        set y to 10
        set z to x plus y
        print z
        end program
        """
        optimized_code = self.optimizer.optimize(code)
        expected_code = """
        start program
        set z to 15
        print z
        end program
        """
        self.assertEqual(optimized_code, expected_code)

    def test_optimize_with_loops(self):
        code = """
        start program
        set x to 0
        repeat 10 times
        increase x by 1
        end repeat
        print x
        end program
        """
        optimized_code = self.optimizer.optimize(code)
        expected_code = """
        start program
        set x to 10
        print x
        end program
        """
        self.assertEqual(optimized_code, expected_code)

    def test_optimize_with_conditionals(self):
        code = """
        start program
        set x to 5
        if x is greater than 10
        print "x is big"
        else
        print "x is small"
        end if
        end program
        """
        optimized_code = self.optimizer.optimize(code)
        expected_code = """
        start program
        print "x is small"
        end program
        """
        self.assertEqual(optimized_code, expected_code)

if __name__ == '__main__':
    unittest.main()
```