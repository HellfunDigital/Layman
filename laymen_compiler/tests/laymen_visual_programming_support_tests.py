```python
import unittest
from laymen_compiler import laymen_visual_programming_support

class TestVisualProgrammingSupport(unittest.TestCase):

    def setUp(self):
        self.visual_support = laymen_visual_programming_support.VisualProgrammingSupport()

    def test_drag_and_drop(self):
        result = self.visual_support.drag_and_drop('button', 'form')
        self.assertEqual(result, 'Button has been added to the form')

    def test_visual_code_blocks(self):
        result = self.visual_support.visual_code_blocks('if', 'condition', 'action')
        self.assertEqual(result, 'If condition block with action has been created')

    def test_visual_error_handling(self):
        result = self.visual_support.visual_error_handling('syntax error')
        self.assertEqual(result, 'Syntax error has been highlighted')

    def test_visual_debugging(self):
        result = self.visual_support.visual_debugging('step over')
        self.assertEqual(result, 'Step over action has been performed')

    def test_visual_api_integration(self):
        result = self.visual_support.visual_api_integration('google maps')
        self.assertEqual(result, 'Google Maps API has been integrated')

if __name__ == '__main__':
    unittest.main()
```