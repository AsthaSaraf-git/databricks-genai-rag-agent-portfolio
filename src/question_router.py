from src.quality_agent import build_quality_agent_response
from src.trend_agent import build_trend_agent_response


def route_question(spark, question):
    question_lower = question.lower()

    if "degraded" in question_lower or "trend" in question_lower:
        return build_trend_agent_response(spark, question)

    if "worst" in question_lower or "quality" in question_lower:
        return build_quality_agent_response(spark, question)

    return """
Supported Questions:
- Which table has the worst data quality?
- Which table quality degraded the most?
"""