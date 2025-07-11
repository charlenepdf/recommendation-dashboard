import pandas as pd
import numpy as np
import os

os.chdir(r"C:\Users\charl\Desktop\recommendation-dashboard")

# Set seed for reproducibility
np.random.seed(1)

# Create 10,000 simulated interactions
n = 10000
df = pd.DataFrame({
    "user_id": np.random.randint(1, 1001, n),
    "item_id": np.random.randint(1, 501, n),
    "timestamp": pd.date_range("2024-01-01", periods=n, freq="min"),
    "clicked": np.random.binomial(1, 0.2, n),
    "converted": np.random.binomial(1, 0.05, n),
    "recommendation_rank": np.random.randint(1, 11, n),
    "user_type": np.random.choice(["new", "returning"], size=n),
    "product_category": np.random.choice(["electronics", "clothing", "books"], size=n),
    "recommendation_cost": np.round(np.random.uniform(0.05, 0.50, n), 2),
    "conversion_value": np.round(np.random.uniform(5, 100, n), 2)
})

# Add A/B test group simulation
df["group"] = np.random.choice(["control", "treatment"], size=len(df))

# Make sure the data folder exists
os.makedirs("data", exist_ok=True)

# Save to CSV
df.to_csv("data/simulated_recommendation_data.csv", index=False)
print("✅ Dataset saved to 'data/simulated_recommendation_data.csv'")