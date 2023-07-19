```python
import json

class IterativeDeveloper:
    def __init__(self):
        self.feedback_data = []

    def collect_feedback(self, feedback):
        self.feedback_data.append(feedback)

    def analyze_feedback(self):
        feedback_summary = {
            'positive': 0,
            'negative': 0,
            'suggestions': []
        }

        for feedback in self.feedback_data:
            if feedback['type'] == 'positive':
                feedback_summary['positive'] += 1
            elif feedback['type'] == 'negative':
                feedback_summary['negative'] += 1

            if 'suggestion' in feedback:
                feedback_summary['suggestions'].append(feedback['suggestion'])

        return feedback_summary

    def save_feedback(self):
        with open('feedback_data.json', 'w') as f:
            json.dump(self.feedback_data, f)

    def load_feedback(self):
        try:
            with open('feedback_data.json', 'r') as f:
                self.feedback_data = json.load(f)
        except FileNotFoundError:
            self.feedback_data = []

    def iterate_development(self, feedback):
        self.collect_feedback(feedback)
        feedback_summary = self.analyze_feedback()
        self.save_feedback()

        return feedback_summary
```