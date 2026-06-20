import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class Project:
    id: int
    last_insight_viewed: datetime

@dataclass
class User:
    id: int
    project_id: int
    last_active: datetime

class InsightLoom:
    def __init__(self):
        self.projects = []
        self.users = []

    def add_project(self, project: Project):
        self.projects.append(project)

    def add_user(self, user: User):
        self.users.append(user)

    def get_map(self) -> int:
        thirty_days_ago = datetime.now() - timedelta(days=30)
        active_projects = [project for project in self.projects if project.last_insight_viewed >= thirty_days_ago]
        return len(active_projects)

    def get_daily_active_users(self) -> int:
        today = datetime.now()
        active_users = [user for user in self.users if user.last_active.date() == today.date()]
        return len(active_users)

    def refresh_data(self, data: dict):
        self.projects = []
        self.users = []
        for project_data in data.get('projects', []):
            project = Project(
                id=project_data['id'],
                last_insight_viewed=datetime.strptime(project_data['last_insight_viewed'], '%Y-%m-%d')
            )
            self.add_project(project)
        for user_data in data.get('users', []):
            user = User(
                id=user_data['id'],
                project_id=user_data['project_id'],
                last_active=datetime.strptime(user_data['last_active'], '%Y-%m-%d')
            )
            self.add_user(user)
