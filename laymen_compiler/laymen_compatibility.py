```python
import platform
from laymen_compiler.laymen_error_handler import ErrorHandler

class Compatibility:
    def __init__(self):
        self.error_handler = ErrorHandler()

    def check_os_compatibility(self):
        """
        Check if the operating system is compatible with Laymen
        """
        if platform.system() not in ['Windows', 'Linux', 'Darwin']:
            self.error_handler.throw_error("Incompatible Operating System. Laymen supports Windows, Linux, and MacOS.")
            return False
        return True

    def check_python_version(self):
        """
        Check if the Python version is compatible with Laymen
        """
        if platform.python_version_tuple() < ('3', '6'):
            self.error_handler.throw_error("Incompatible Python version. Laymen requires Python 3.6 or higher.")
            return False
        return True

    def check_library_compatibility(self, library):
        """
        Check if a specific library is compatible with Laymen
        """
        # This is a placeholder. Actual implementation would depend on the libraries Laymen is expected to work with.
        compatible_libraries = ['numpy', 'pandas', 'matplotlib']
        if library not in compatible_libraries:
            self.error_handler.throw_error(f"Incompatible library. {library} is not supported by Laymen.")
            return False
        return True

    def check_all(self):
        """
        Check all compatibility requirements
        """
        return self.check_os_compatibility() and self.check_python_version()
```