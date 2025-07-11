import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set Streamlit page config
st.set_page_config(page_title="Recommendation Dashboard", layout="wide")

# File upload
uploaded_file = st.sidebar.file_uploader("Upload your own CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Custom data uploaded successfully")
else:
    df = pd.read_csv("data/simulated_recommendation_data.csv")
    st.caption("Using simulated data from /data folder")


# Filters
st.sidebar.title("Filters")
user_type = st.sidebar.multiselect("User Type", options=df["user_type"].unique(), default=df["user_type"].unique())
product_category = st.sidebar.multiselect("Product Category", options=df["product_category"].unique(), default=df["product_category"].unique())

# Apply filters
filtered_df = df[
    (df["user_type"].isin(user_type)) &
    (df["product_category"].isin(product_category))
]

# KPIs
ctr = filtered_df["clicked"].mean()
conversion_rate = filtered_df[filtered_df["clicked"] == 1]["converted"].mean()
roi = (filtered_df["conversion_value"].sum() - filtered_df["recommendation_cost"].sum()) / filtered_df["recommendation_cost"].sum()

# Display KPIs
st.title("Recommendation System Evaluation Dashboard")
st.metric("Click-Through Rate (CTR)", f"{ctr:.2%}")
st.metric("Conversion Rate", f"{conversion_rate:.2%}")
st.metric("ROI", f"{roi:.2f}")

# Business insight note
st.markdown("""
> These metrics help identify the most effective recommendation ranks, optimize campaigns for different user cohorts, and quantify ROI for B2B clients evaluating system performance.
""")

# A/B Test Group CTR Comparison
if "group" in filtered_df.columns:
    st.subheader("CTR by A/B Test Group")
    group_ctr = filtered_df.groupby("group")["clicked"].mean().reset_index()
    st.bar_chart(group_ctr.set_index("group"))

    st.subheader("Conversion Rate by A/B Test Group")
    group_conv = filtered_df[filtered_df["clicked"] == 1].groupby("group")["converted"].mean().reset_index()
    st.bar_chart(group_conv.set_index("group"))

# Plot CTR over time
df["timestamp"] = pd.to_datetime(df["timestamp"])
filtered_df["timestamp"] = pd.to_datetime(filtered_df["timestamp"])  # ensure correct dtype
filtered_df.set_index("timestamp", inplace=True)  # make timestamp the index
ctr_over_time = filtered_df["clicked"].resample("D").mean().reset_index()
fig_ctr = px.line(ctr_over_time, x="timestamp", y="clicked", title="CTR Over Time")
st.plotly_chart(fig_ctr, use_container_width=True)

# Conversion by recommendation rank
rank_chart = filtered_df.groupby("recommendation_rank")["converted"].mean().reset_index()
fig_rank = px.bar(rank_chart, x="recommendation_rank", y="converted", title="Conversion Rate by Recommendation Rank")
st.plotly_chart(fig_rank, use_container_width=True)

# ROI by Product Category
roi_by_category = (
    filtered_df.groupby("product_category")[["recommendation_cost", "conversion_value"]]
    .apply(lambda x: (x["conversion_value"].sum() - x["recommendation_cost"].sum()) / x["recommendation_cost"].sum())
    .reset_index(name="ROI")
)

fig_roi = px.bar(
    roi_by_category,
    x="product_category",
    y="ROI",
    title="ROI by Product Category"
)
st.plotly_chart(fig_roi, use_container_width=True)
