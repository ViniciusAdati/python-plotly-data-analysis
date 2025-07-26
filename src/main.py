import pandas as pd
import plotly.express as px
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

os.makedirs(OUTPUT_DIR, exist_ok=True)

users_file = os.path.join(DATA_DIR, 'internet_users_by_country.csv')
population_file = os.path.join(DATA_DIR, 'population_by_country.csv')

try:
    df_users = pd.read_csv(users_file)
    df_population = pd.read_csv(population_file)
except FileNotFoundError as e:
    print(f"Error: Could not find a data file. {e}")
    sys.exit(1)

print("Merging internet users and population data...")
df = pd.merge(df_users, df_population, on='Country', how='inner')

df['Penetration_Rate'] = (df['Internet_Users'] / df['Population']) * 100
df['Penetration_Rate'] = df['Penetration_Rate'].round(2)

print("Data merged and prepared successfully. Generating plots...")

df_sorted = df.sort_values(by='Internet_Users', ascending=False)
top_20_countries = df_sorted.head(20)

fig_2d = px.bar(top_20_countries, x='Country', y='Internet_Users', title='Top 20 Countries by Number of Internet Users')
output_path_2d = os.path.join(OUTPUT_DIR, '2d_top_20_internet_users.html')
fig_2d.write_html(output_path_2d)
print(f"2D plot saved to: {output_path_2d}")

fig_3d = px.scatter_3d(
    df,
    x='Population',
    y='Internet_Users',
    z='Penetration_Rate',
    color='Country',
    hover_name='Country',
    title='Population vs. Internet Users vs. Penetration Rate',
    labels={
        'Population': 'Total Population',
        'Internet_Users': 'Number of Internet Users',
        'Penetration_Rate': 'Penetration Rate (%)'
    }
)
fig_3d.update_layout(showlegend=False)
output_path_3d = os.path.join(OUTPUT_DIR, '3d_internet_analysis.html')
fig_3d.write_html(output_path_3d)
print(f"3D plot saved to: {output_path_3d}")

print("\nProcess finished successfully!")