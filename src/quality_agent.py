from pyspark.sql.functions import col


def get_worst_quality_table(spark):
    quality_df = spark.table("workspace.default.gold_quality_by_table")

    return (
        quality_df
        .orderBy(col("quality_score").asc())
        .limit(1)
        .collect()[0]
    )


def get_failed_rules(spark, table_name):
    rule_df = spark.table("workspace.default.gold_quality_by_rule")

    return (
        rule_df
        .filter(col("table_name") == table_name)
        .orderBy(col("total_failure_percentage").desc())
        .collect()
    )


def build_quality_agent_response(spark, user_question):
    worst = get_worst_quality_table(spark)
    table_name = worst["table_name"]
    failed_rules = get_failed_rules(spark, table_name)

    response = f"""
Question:
{user_question}

Answer:
The table with the worst data quality is `{table_name}`.

Reason:
- Quality Score: {worst["quality_score"]}
- Failed Rules: {worst["failed_rules"]}
- Total Rules: {worst["total_rules"]}

Top failed rule areas:
"""

    for rule in failed_rules:
        response += f"""
- Rule: {rule["rule"]}
  Failure Percentage: {rule["total_failure_percentage"]}
"""

    response += """

Recommended Actions:
- Add validation checks earlier in Bronze/Silver.
- Add deduplication for uniqueness failures.
- Add mandatory checks for not-null failures.
- Track recurring issues historically.
"""

    return response