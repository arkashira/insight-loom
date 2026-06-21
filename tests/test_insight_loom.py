import pytest
from src.insight_loom import generate_insights, visualize_insights, Insight

def test_generate_insights():
    data = [1.0, 2.0, 3.0, 2.0, 1.0]
    insights = generate_insights(data)
    assert len(insights) == 4
    assert insights[0].description == "Increase"
    assert insights[2].description == "Decrease"

def test_generate_insights_empty():
    data = []
    insights = generate_insights(data)
    assert len(insights) == 0

def test_visualize_insights():
    insights = [Insight(0, "Increase", [1.0, 2.0]), Insight(1, "Decrease", [2.0, 1.0])]
    visualization = visualize_insights(insights)
    assert "Insight 0: Increase (1.0 -> 2.0)" in visualization
    assert "Insight 1: Decrease (2.0 -> 1.0)" in visualization

def test_visualize_insights_empty():
    insights = []
    visualization = visualize_insights(insights)
    assert visualization == ""
