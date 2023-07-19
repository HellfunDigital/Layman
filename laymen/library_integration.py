```python
# laymen/library_integration.py

import importlib

class LibraryIntegration:
    def __init__(self):
        self.libraries = {}

    def import_library(self, library_name):
        try:
            library = importlib.import_module(library_name)
            self.libraries[library_name] = library
            print(f"Library '{library_name}' has been successfully imported.")
        except ImportError:
            print(f"Failed to import library '{library_name}'. Please make sure it is installed and try again.")

    def use_library(self, library_name, function_name, *args, **kwargs):
        if library_name in self.libraries:
            library = self.libraries[library_name]
            if hasattr(library, function_name):
                function = getattr(library, function_name)
                return function(*args, **kwargs)
            else:
                print(f"Function '{function_name}' does not exist in library '{library_name}'.")
        else:
            print(f"Library '{library_name}' has not been imported. Please import it before using.")

    def list_libraries(self):
        return list(self.libraries.keys())
```