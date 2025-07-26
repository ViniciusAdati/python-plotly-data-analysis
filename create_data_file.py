import pandas as pd
import os

DATA_DIR = 'data'
os.makedirs(DATA_DIR, exist_ok=True)

data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam', 'Printer', 'Gaming Chair', 'Office Desk'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories', 'Electronics', 'Furniture', 'Furniture'],
    'Units_Sold': [150, 300, 250, 180, 400, 90, 120, 100],
    'Unit_Price': [1200, 25, 75, 300, 60, 180, 450, 250],
    'Customer_Rating': [4.5, 4.7, 4.6, 4.4, 4.8, 4.3, 4.9, 4.5]
}
df = pd.DataFrame(data)

df['Total_Revenue'] = df['Units_Sold'] * df['Unit_Price']

file_path = os.path.join(DATA_DIR, 'sample_data.xlsx')

df.to_excel(file_path, index=False, engine='openpyxl')
