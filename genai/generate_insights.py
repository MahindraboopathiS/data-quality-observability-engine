import sqlite3
from openai import OpenAI

client = OpenAI()  # assumes API key set

conn = sqlite3.connect("data/pipeline.db")
df = conn.execute("""
    SELECT check_name, result_count, severity
    FROM data_quality_logs
    ORDER BY run_timestamp DESC
""").fetchall()

summary = "\n".join([f"{row[0]}: {row[1]}" for row in df])

prompt = f"""
You are a data analyst.

Here are data quality check results:
{summary}

Write a concise business summary:
- What are the biggest issues?
- Why do they matter?
- What actions should be taken?
"""

response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)