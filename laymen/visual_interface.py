```python
import tkinter as tk
from tkinter import messagebox
from laymen.parser import Parser
from laymen.error_handling import ErrorHandler

class VisualInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Laymen Programming Language")
        self.parser = Parser()
        self.error_handler = ErrorHandler()

        self.code_text = tk.Text(self.root)
        self.code_text.pack()

        self.run_button = tk.Button(self.root, text="Run", command=self.run_code)
        self.run_button.pack()

    def run_code(self):
        code = self.code_text.get("1.0", tk.END)
        try:
            self.parser.parse(code)
        except Exception as e:
            self.error_handler.handle(e)
            messagebox.showerror("Error", str(e))

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    interface = VisualInterface()
    interface.start()
```