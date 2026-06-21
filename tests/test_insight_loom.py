import pytest
from insight_loom import generate_insight_report, export_report_to_pdf

def test_generate_insight_report():
    start_date = "2022-01-01"
    end_date = "2022-01-31"
    data_sources = ["source1", "source2"]
    report = generate_insight_report(start_date, end_date, data_sources)
    assert len(report.trends) == 3
    assert len(report.sentiment_shifts) == 2
    assert len(report.action_recommendations) == 1

def test_export_report_to_pdf():
    report = generate_insight_report("2022-01-01", "2022-01-31", ["source1", "source2"])
    pdf_content = export_report_to_pdf(report)
    assert "Insight Report" in pdf_content
    assert "Trends:" in pdf_content
    assert "Sentiment Shifts:" in pdf_content
    assert "Action Recommendations:" in pdf_content

def test_generate_insight_report_edge_case():
    start_date = "2022-02-30"
    end_date = "2022-01-31"
    data_sources = ["source1", "source2"]
    with pytest.raises(ValueError):
        generate_insight_report(start_date, end_date, data_sources)

def test_export_report_to_pdf_edge_case():
    report = None
    with pytest.raises(AttributeError):
        export_report_to_pdf(report)
