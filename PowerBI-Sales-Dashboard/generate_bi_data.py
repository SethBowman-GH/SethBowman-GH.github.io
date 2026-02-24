import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create Sales Fact Table
np.random.seed(42)
num_rows = 1000
data = {
    'OrderID': range(1001, 1001 + num_rows),
    'OrderDate': [datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(num_rows)],
    'ProductID': np.random.randint(1, 50, num_rows),
    'CustomerID': np.random.randint(1, 100, num_rows),
    'Sales': np.random.uniform(100, 5000, num_rows).round(2),
    'Quantity': np.random.randint(1, 10, num_rows)
}
df = pd.DataFrame(data)
df['Profit'] = (df['Sales'] * np.random.uniform(0.05, 0.25, num_rows)).round(2)

# Save to CSV
df.to_csv('Executive_Sales_Data.csv', index=False)
print("Dataset Created Successfully")
