```python
import json
from typing import Dict

class CommunitySupport:
    def __init__(self):
        self.communityData = []

    def load_community_data(self, filename: str):
        with open(filename, 'r') as file:
            self.communityData = json.load(file)

    def save_community_data(self, filename: str):
        with open(filename, 'w') as file:
            json.dump(self.communityData, file)

    def add_project(self, project: Dict):
        self.communityData.append(project)
        self.save_community_data('community_data.json')

    def get_projects(self):
        return self.communityData

    def get_project(self, project_id: int):
        for project in self.communityData:
            if project['id'] == project_id:
                return project
        return None

    def update_project(self, project_id: int, updated_project: Dict):
        for i, project in enumerate(self.communityData):
            if project['id'] == project_id:
                self.communityData[i] = updated_project
                self.save_community_data('community_data.json')
                return True
        return False

    def delete_project(self, project_id: int):
        for i, project in enumerate(self.communityData):
            if project['id'] == project_id:
                del self.communityData[i]
                self.save_community_data('community_data.json')
                return True
        return False
```