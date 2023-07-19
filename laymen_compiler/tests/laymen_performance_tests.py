```python
import unittest
from laymen_compiler import laymen_compiler
from laymen_compiler import laymen_performance

class TestLaymenPerformance(unittest.TestCase):

    def setUp(self):
        self.compiler = laymen_compiler.LaymenCompiler()
        self.performance = laymen_performance.LaymenPerformance()

    def test_compile_time(self):
        code = """
        start program
        set x to 5
        set y to 10
        set z to x plus y
        print z
        end program
        """
        start_time = time.time()
        self.compiler.compile(code)
        end_time = time.time()
        compile_time = end_time - start_time
        self.assertTrue(self.performance.check_compile_time(compile_time))

    def test_run_time(self):
        code = """
        start program
        set x to 5
        set y to 10
        set z to x plus y
        print z
        end program
        """
        compiled_code = self.compiler.compile(code)
        start_time = time.time()
        self.compiler.run(compiled_code)
        end_time = time.time()
        run_time = end_time - start_time
        self.assertTrue(self.performance.check_run_time(run_time))

    def test_memory_usage(self):
        code = """
        start program
        set x to 5
        set y to 10
        set z to x plus y
        print z
        end program
        """
        compiled_code = self.compiler.compile(code)
        memory_usage = self.performance.get_memory_usage(compiled_code)
        self.assertTrue(self.performance.check_memory_usage(memory_usage))

if __name__ == '__main__':
    unittest.main()
```