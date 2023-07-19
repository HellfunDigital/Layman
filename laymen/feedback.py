```python
class Feedback:
    def __init__(self):
        self.feedback_list = []

    class FeedbackType:
        BUG_REPORT = "Bug Report"
        FEATURE_REQUEST = "Feature Request"
        GENERAL_FEEDBACK = "General Feedback"

    class FeedbackEntry:
        def __init__(self, feedback_type, description, user):
            self.feedback_type = feedback_type
            self.description = description
            self.user = user

    def add_feedback(self, feedback_type, description, user):
        new_feedback = self.FeedbackEntry(feedback_type, description, user)
        self.feedback_list.append(new_feedback)

    def get_all_feedback(self):
        return self.feedback_list

    def get_feedback_by_type(self, feedback_type):
        return [feedback for feedback in self.feedback_list if feedback.feedback_type == feedback_type]

    def get_feedback_by_user(self, user):
        return [feedback for feedback in self.feedback_list if feedback.user == user]
```