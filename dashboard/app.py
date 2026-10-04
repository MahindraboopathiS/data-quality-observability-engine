import sqlite3
import pandas as pd
import streamlit as st

conn = sqlite3.connect("data/pipeline.db")

df = pd.read_sql("SELECT * FROM data_quality_logs", conn)

st.title("Data Quality Monitoring Dashboard")

# Errors over time
st.subheader("Errors Over Time")
errors_over_time = df.groupby("run_timestamp")["result_count"].sum().reset_index()
st.line_chart(errors_over_time.set_index("run_timestamp"))

# Error breakdown
st.subheader("Errors by Type")
error_type = df.groupby("check_name")["result_count"].sum().reset_index()
st.bar_chart(error_type.set_index("check_name"))

# Severity breakdown
st.subheader("Errors by Severity")
severity = df.groupby("severity")["result_count"].sum().reset_index()
st.bar_chart(severity.set_index("severity"))

conn.close()