import streamlit as st
import pandas as pd

st.set_page_config(page_title="OSINT Threat Intelligence", layout="wide")

st.title("🛡️ AI-Powered OSINT Threat Intelligence Dashboard")

# Load data
df = pd.read_csv("risk_output.csv")

# Sidebar filter
st.sidebar.header("Filter Options")
risk_filter = st.sidebar.selectbox("Select Risk Level", ["All", "High", "Medium", "Low"])

# Apply filter
if risk_filter != "All":
    df_filtered = df[df["risk_level"] == risk_filter]
else:
    df_filtered = df

# Metrics
st.subheader("📊 Risk Summary")
col1, col2, col3 = st.columns(3)

col1.metric("High Risk", len(df[df["risk_level"] == "High"]))
col2.metric("Medium Risk", len(df[df["risk_level"] == "Medium"]))
col3.metric("Low Risk", len(df[df["risk_level"] == "Low"]))

# Table
st.subheader("📄 Threat Intelligence Feed")
st.dataframe(df_filtered[["text", "risk_level", "final_score"]])

# Top risks
st.subheader("🔝 Top Risks")
top_risks = df.sort_values(by="final_score", ascending=False).head(5)
st.dataframe(top_risks[["text", "risk_level", "final_score"]])
