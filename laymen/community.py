```python
class Community:
    def __init__(self):
        self.users = []
        self.projects = []
        self.questions = []

    def add_user(self, user):
        self.users.append(user)

    def add_project(self, project):
        self.projects.append(project)

    def add_question(self, question):
        self.questions.append(question)

    def get_users(self):
        return self.users

    def get_projects(self):
        return self.projects

    def get_questions(self):
        return self.questions

class User:
    def __init__(self, name):
        self.name = name
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def get_projects(self):
        return self.projects

class Project:
    def __init__(self, name, user):
        self.name = name
        self.user = user
        self.code = ""

    def set_code(self, code):
        self.code = code

    def get_code(self):
        return self.code

class Question:
    def __init__(self, user, question):
        self.user = user
        self.question = question

    def get_question(self):
        return self.question
```