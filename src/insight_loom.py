import json
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Insight:
    id: int
    message: str
    dismissed: bool = False
    snoozed_until: datetime = None

class InsightLoom:
    def __init__(self):
        self.insights = []
        self.dismissed_insights = []

    def add_insight(self, insight):
        self.insights.append(insight)

    def dismiss_insight(self, insight_id):
        for insight in self.insights:
            if insight.id == insight_id:
                self.dismissed_insights.append(insight)
                self.insights.remove(insight)
                return

    def snooze_insight(self, insight_id):
        for insight in self.insights:
            if insight.id == insight_id:
                insight.snoozed_until = datetime.now() + timedelta(hours=24)
                return

    def get_insights(self):
        return [insight for insight in self.insights if insight.snoozed_until is None or insight.snoozed_until < datetime.now()]
