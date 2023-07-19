```python
import requests
from laymen.error_handling import handle_error

class APIIntegration:
    def __init__(self):
        self.api_names = ["API1", "API2", "API3"]

    def use_api(self, api_name, endpoint, method="GET", data=None):
        if api_name not in self.api_names:
            handle_error(f"Unknown API: {api_name}")
            return

        if method == "GET":
            response = requests.get(f"https://{api_name}.com/{endpoint}")
        elif method == "POST":
            response = requests.post(f"https://{api_name}.com/{endpoint}", data=data)
        else:
            handle_error(f"Unsupported method: {method}")
            return

        if response.status_code != 200:
            handle_error(f"API request failed with status code {response.status_code}")
            return

        return response.json()

api_integration = APIIntegration()
```