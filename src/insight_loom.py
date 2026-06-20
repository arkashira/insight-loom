import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class Insight:
    name: str
    link: str
    data: str

class InsightLoom:
    def __init__(self):
        self.insights = []
        self.last_updated = datetime.now()

    def add_insight(self, insight: Insight):
        self.insights.append(insight)

    def get_top_insights(self) -> List[Insight]:
        return self.insights[:3]

    def refresh_insights(self):
        self.last_updated = datetime.now()
        # Simulate refreshing insights
        self.insights = [
            Insight("Risk Alert", "https://example.com/risk", "High risk detected"),
            Insight("Opportunity Highlight", "https://example.com/opportunity", "New opportunity found"),
            Insight("Team Sentiment", "https://example.com/sentiment", "Team sentiment is positive")
        ]

    def is_stale(self) -> bool:
        return datetime.now() - self.last_updated > timedelta(minutes=5)
