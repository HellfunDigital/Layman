```python
import json

class TutorialGenerator:
    def __init__(self):
        self.tutorialContent = []

    def generate_tutorial(self):
        # Basic tutorial content
        self.tutorialContent.append({
            "title": "Introduction to Laymen",
            "content": "Laymen is a programming language designed for non-programmers. It uses English-like syntax to make it easy to understand and write code."
        })
        self.tutorialContent.append({
            "title": "Variables in Laymen",
            "content": "In Laymen, you can create variables to store data. For example, 'Create a variable named age and set it to 25.'"
        })
        self.tutorialContent.append({
            "title": "Loops in Laymen",
            "content": "Loops are used to repeat actions. For example, 'Repeat 10 times: print 'Hello, world!''"
        })
        self.tutorialContent.append({
            "title": "Conditionals in Laymen",
            "content": "Conditionals are used to make decisions in the code. For example, 'If the age is greater than 18, print 'You are an adult.''"
        })
        self.tutorialContent.append({
            "title": "Functions in Laymen",
            "content": "Functions are reusable pieces of code. For example, 'Create a function named greet that takes a name and prints 'Hello, ' followed by the name.'"
        })

    def get_tutorial_content(self):
        return self.tutorialContent

    def save_tutorial_content(self):
        with open('tutorialContent.json', 'w') as file:
            json.dump(self.tutorialContent, file)

tutorialGenerator = TutorialGenerator()
tutorialGenerator.generate_tutorial()
tutorialContent = tutorialGenerator.get_tutorial_content()
tutorialGenerator.save_tutorial_content()
```