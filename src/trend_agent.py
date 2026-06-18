from pyspark.sql.functions import col


def get_most_degraded_table(spark):
    trend_df = spark.table("workspace.default.gold_quality_trends")

    return (
        trend_df
        .filter(col("quality_score_change").isNotNull())
        .orderBy(col("quality_score_change").asc())
        .limit(1)
        .collect()[0]
    )


def build_trend_agent_response(spark, user_question):
    result = get_most_degraded_table(spark)

    return f"""
Question:
{user_question}

Answer:
The table with the highest quality degradation is `{result["table_name"]}`.

Trend Evidence:
- Previous Quality Score: {result["previous_quality_score"]}
- Current Quality Score: {result["quality_score"]}
- Quality Score Change: {result["quality_score_change"]}
- Run Timestamp: {result["run_timestamp"]}

Recommended Actions:
- Compare failed rules between previous and current runs.
- Check new null, duplicate, schema, or accepted-value failures.
- Review recent ingestion or transformation changes.
- Add alerting when quality score drops beyond threshold.
"""