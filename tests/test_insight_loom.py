from insight_loom import InsightLoom, Project, User
import pytest
from datetime import datetime, timedelta

def test_get_map():
    insight_loom = InsightLoom()
    project1 = Project(1, datetime.now())
    project2 = Project(2, datetime.now() - timedelta(days=31))
    insight_loom.add_project(project1)
    insight_loom.add_project(project2)
    assert insight_loom.get_map() == 1

def test_get_daily_active_users():
    insight_loom = InsightLoom()
    user1 = User(1, 1, datetime.now())
    user2 = User(2, 1, datetime.now() - timedelta(days=1))
    insight_loom.add_user(user1)
    insight_loom.add_user(user2)
    assert insight_loom.get_daily_active_users() == 1

def test_refresh_data():
    insight_loom = InsightLoom()
    data = {
        'projects': [
            {'id': 1, 'last_insight_viewed': '2024-09-16'},
            {'id': 2, 'last_insight_viewed': '2024-08-16'}
        ],
        'users': [
            {'id': 1, 'project_id': 1, 'last_active': '2024-09-16'},
            {'id': 2, 'project_id': 1, 'last_active': '2024-09-15'}
        ]
    }
    insight_loom.refresh_data(data)
    assert len(insight_loom.projects) == 2
    assert len(insight_loom.users) == 2

def test_get_map_edge_case():
    insight_loom = InsightLoom()
    project1 = Project(1, datetime.now())
    project2 = Project(2, datetime.now())
    insight_loom.add_project(project1)
    insight_loom.add_project(project2)
    assert insight_loom.get_map() == 2

def test_get_daily_active_users_edge_case():
    insight_loom = InsightLoom()
    user1 = User(1, 1, datetime.now())
    user2 = User(2, 1, datetime.now())
    insight_loom.add_user(user1)
    insight_loom.add_user(user2)
    assert insight_loom.get_daily_active_users() == 2
