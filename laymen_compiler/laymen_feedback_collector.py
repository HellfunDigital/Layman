```python
import json

class FeedbackCollector:
    def __init__(self):
        self.feedbackData = []

    def collect_feedback(self, feedback):
        self.feedbackData.append(feedback)
        self.save_feedback()

    def save_feedback(self):
        with open('feedbackData.json', 'w') as f:
            json.dump(self.feedbackData, f)

    def load_feedback(self):
        try:
            with open('feedbackData.json', 'r') as f:
                self.feedbackData = json.load(f)
        except FileNotFoundError:
            self.feedbackData = []

    def get_feedback(self):
        self.load_feedback()
        return self.feedbackData
```