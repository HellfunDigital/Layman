```python
import unittest
from laymen_compiler import laymen_api_integration

class TestAPIIntegration(unittest.TestCase):

    def setUp(self):
        self.api_integration = laymen_api_integration.APIIntegration()

    def test_api_call(self):
        response = self.api_integration.api_call('https://api.github.com')
        self.assertEqual(response.status_code, 200)

    def test_api_integration(self):
        result = self.api_integration.integrate('https://api.github.com/users/octocat')
        self.assertEqual(result['login'], 'octocat')

    def test_error_handling(self):
        with self.assertRaises(Exception):
            self.api_integration.api_call('https://nonexistentapi.com')

if __name__ == '__main__':
    unittest.main()
```