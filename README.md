# Recommendation System Evaluation Dashboard

A simulation-based analytics dashboard for evaluating product recommendation systems, inspired by BytePlus Recommend.

## Project Overview

This project simulates recommendation system data and analyzes key performance metrics such as:
- Click-Through Rate (CTR)
- Conversion Rate
- Return on Investment (ROI)
- Cohort-based user engagement

Built using **Python + Streamlit**, this dashboard emulates the performance reporting you'd see in a real-world B2B recommendation analytics tool.

## Features

- Charts for CTR over time, ROI by product category, and conversion rates by rank
- Simulated control vs. treatment group for A/B testing concepts
- Filter by date range, user segment, and product category
- Upload external CSVs for side-by-side KPI comparison

## Dataset

The dataset is synthetically generated using Python. Each row contains:
- `user_id`, `item_id`, `timestamp`
- `clicked`, `converted`, `recommendation_rank`
- `user_type` (new/returning), `product_category`
- `recommendation_cost`, `conversion_value`

## Dashboard Preview



## Why It Matters

Understanding how to measure and optimize product recommendations is essential in modern e-commerce and B2B SaaS. This project simulates real-world metrics and shows how decision-makers can act on them.

## Tech Stack

- Python, Pandas, NumPy
- Streamlit
- Matplotlib/Altair/Plotly (for visualization)
