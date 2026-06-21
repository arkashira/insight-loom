import json
from dataclasses import dataclass
from typing import List

@dataclass
class Insight:
    id: int
    description: str
    data: List[float]

def generate_insights(data: List[float]) -> List[Insight]:
    insights = []
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            insights.append(Insight(i, "Decrease", [data[i], data[i + 1]]))
        elif data[i] < data[i + 1]:
            insights.append(Insight(i, "Increase", [data[i], data[i + 1]]))
    return insights

def visualize_insights(insights: List[Insight]) -> str:
    visualization = ""
    for insight in insights:
        visualization += f"Insight {insight.id}: {insight.description} ({insight.data[0]} -> {insight.data[1]})\n"
    return visualization
