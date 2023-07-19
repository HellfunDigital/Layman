```python
class LaymenTutorial:
    def __init__(self):
        self.tutorials = []

    def add_tutorial(self, title, content):
        self.tutorials.append({'title': title, 'content': content})

    def get_tutorial(self, title):
        for tutorial in self.tutorials:
            if tutorial['title'] == title:
                return tutorial
        return None

    def list_tutorials(self):
        return [tutorial['title'] for tutorial in self.tutorials]

# Initialize LaymenTutorial object
laymen_tutorial = LaymenTutorial()

# Add tutorials
laymen_tutorial.add_tutorial("Introduction to Laymen", "This tutorial introduces the basics of Laymen...")
laymen_tutorial.add_tutorial("Laymen Syntax", "This tutorial covers the syntax of Laymen...")
laymen_tutorial.add_tutorial("Building Applications with Laymen", "This tutorial guides you through building a simple application with Laymen...")

# Get a specific tutorial
print(laymen_tutorial.get_tutorial("Introduction to Laymen"))

# List all tutorials
print(laymen_tutorial.list_tutorials())
```