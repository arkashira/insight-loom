from datetime import datetime, timedelta
from insight_loom import Insight, InsightLoom
import pytest

def test_add_insight():
    insight_loom = InsightLoom()
    insight = Insight("Test Insight", "https://example.com/test", "Test data")
    insight_loom.add_insight(insight)
    assert len(insight_loom.insights) == 1
    assert insight_loom.insights[0].name == "Test Insight"

def test_get_top_insights():
    insight_loom = InsightLoom()
    insight_loom.add_insight(Insight("Test Insight 1", "https://example.com/test1", "Test data 1"))
    insight_loom.add_insight(Insight("Test Insight 2", "https://example.com/test2", "Test data 2"))
    insight_loom.add_insight(Insight("Test Insight 3", "https://example.com/test3", "Test data 3"))
    top_insights = insight_loom.get_top_insights()
    assert len(top_insights) == 3
    assert top_insights[0].name == "Test Insight 1"
    assert top_insights[1].name == "Test Insight 2"
    assert top_insights[2].name == "Test Insight 3"

def test_refresh_insights():
    insight_loom = InsightLoom()
    insight_loom.refresh_insights()
    assert len(insight_loom.insights) == 3
    assert insight_loom.insights[0].name == "Risk Alert"
    assert insight_loom.insights[1].name == "Opportunity Highlight"
    assert insight_loom.insights[2].name == "Team Sentiment"

def test_is_stale():
    insight_loom = InsightLoom()
    insight_loom.last_updated = datetime.now() - timedelta(minutes=10)
    assert insight_loom.is_stale() == True
    insight_loom.last_updated = datetime.now()
    assert insight_loom.is_stale() == False
