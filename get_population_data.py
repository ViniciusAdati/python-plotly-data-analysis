import pandas as pd
import os
import sys

URL = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
OUTPUT_DIR = 'data'
CSV_FILE_PATH = os.path.join(OUTPUT_DIR, 'population_by_country.csv')

os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_population_data():
    print(f"Fetching population data from: {URL}")
    try:
        list_of_dataframes = pd.read_html(URL)
        df = list_of_dataframes[0]

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(1)

        df.rename(columns={'Location': 'Country', 'Population': 'Population'}, inplace=True)

        df = df[['Country', 'Population']].copy()

        df['Population'] = df['Population'].astype(str).str.replace(r'\[.*?\]', '', regex=True)
        df['Population'] = df['Population'].str.replace(',', '', regex=False)
        df['Population'] = pd.to_numeric(df['Population'], errors='coerce')
        
        df.dropna(inplace=True)

        df.to_csv(CSV_FILE_PATH, index=False, encoding='utf-8')
        print("-" * 50)
        print(f"Success! Population data saved to: {CSV_FILE_PATH}")
        print("-" * 50)
        print(df.head())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_population_data()