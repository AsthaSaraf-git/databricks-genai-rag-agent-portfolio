import ollama

with open("ollama/sample_agent_evidence.txt", "r") as f:
    tool_output = f.read()

question = "Which table quality degraded the most and what is the likely business impact?"

prompt = f"""
You are a Senior Data Quality Architect.

User Question:
{question}

Evidence from Databricks Tools:
{tool_output}

Using only this evidence, provide:
1. Executive Summary
2. Root Cause
3. Business Impact
4. Recommended Actions

Rules:
- Use only the supplied evidence.
- Do not invent percentages, revenue impact, customer impact, or quantified business impact.
- If evidence is insufficient, explicitly state what additional data is required.
- Clearly separate facts from assumptions.
- Do not make up numbers.
"""

response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

output_text = response["message"]["content"]

print(output_text)

with open("ollama/quality_analysis_output.txt", "w") as f:
    f.write(output_text)

print("\nResponse saved to: ollama/quality_analysis_output.txt")