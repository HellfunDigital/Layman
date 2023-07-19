```python
import unittest
from laymen_compiler import laymen_iterative_development

class TestIterativeDevelopment(unittest.TestCase):

    def setUp(self):
        self.iterative_dev = laymen_iterative_development.IterativeDevelopment()

    def test_collect_feedback(self):
        feedback = "I found it difficult to understand the syntax."
        self.iterative_dev.collect_feedback(feedback)
        self.assertIn(feedback, self.iterative_dev.feedback_list)

    def test_implement_feedback(self):
        feedback = "The error messages are not clear."
        self.iterative_dev.collect_feedback(feedback)
        self.iterative_dev.implement_feedback()
        self.assertNotIn(feedback, self.iterative_dev.feedback_list)

    def test_iterate_language_design(self):
        initial_design = self.iterative_dev.language_design
        self.iterative_dev.iterate_language_design()
        self.assertNotEqual(initial_design, self.iterative_dev.language_design)

if __name__ == '__main__':
    unittest.main()
```