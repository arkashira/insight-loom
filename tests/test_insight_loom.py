from insight_loom import Insight, InsightLoom
import pytest
from datetime import datetime, timedelta

def test_add_insight():
    loom = InsightLoom()
    insight = Insight(1, "Test insight")
    loom.add_insight(insight)
    assert len(loom.insights) == 1

def test_dismiss_insight():
    loom = InsightLoom()
    insight = Insight(1, "Test insight")
    loom.add_insight(insight)
    loom.dismiss_insight(1)
    assert len(loom.insights) == 0
    assert len(loom.dismissed_insights) == 1

def test_snooze_insight():
    loom = InsightLoom()
    insight = Insight(1, "Test insight")
    loom.add_insight(insight)
    loom.snooze_insight(1)
    assert loom.insights[0].snoozed_until is not None

def test_get_insights():
    loom = InsightLoom()
    insight1 = Insight(1, "Test insight 1")
    insight2 = Insight(2, "Test insight 2")
    loom.add_insight(insight1)
    loom.add_insight(insight2)
    loom.snooze_insight(1)
    assert len(loom.get_insights()) == 1

def test_get_insights_after_snooze():
    loom = InsightLoom()
    insight = Insight(1, "Test insight")
    loom.add_insight(insight)
    loom.snooze_insight(1)
    insight.snoozed_until = datetime.now() - timedelta(hours=1)
    assert len(loom.get_insights()) == 1
