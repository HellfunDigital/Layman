```python
import requests
from laymen_error_handler import ErrorHandler

class APIIntegration:
    def __init__(self):
        self.error_handler = ErrorHandler()

    def get_request(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            self.error_handler.handle_error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.error_handler.handle_error(f'Other error occurred: {err}')

    def post_request(self, url, data):
        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            self.error_handler.handle_error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.error_handler.handle_error(f'Other error occurred: {err}')

    def put_request(self, url, data):
        try:
            response = requests.put(url, data=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            self.error_handler.handle_error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.error_handler.handle_error(f'Other error occurred: {err}')

    def delete_request(self, url):
        try:
            response = requests.delete(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            self.error_handler.handle_error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.error_handler.handle_error(f'Other error occurred: {err}')
```