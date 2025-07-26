import pandas as pd
import os
import sys

URL = "https://en.wikipedia.org/wiki/List_of_countries_by_number_of_Internet_users"
OUTPUT_DIR = 'data'
CSV_FILE_PATH = os.path.join(OUTPUT_DIR, 'internet_users_by_country.csv')

os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_and_save_internet_data():
    print(f"Fetching data from: {URL}")

    try:
        list_of_dataframes = pd.read_html(URL)
        print("Selecting the correct data table (index 4)...")
        df = list_of_dataframes[4]

        df.rename(columns={
            'Location': 'Country',
            'Users (CIA)': 'Internet_Users'
        }, inplace=True)
        
        df = df[['Country', 'Internet_Users']].copy()

        df['Internet_Users'] = df['Internet_Users'].astype(str).str.replace(r'\[.*?\]', '', regex=True)
        df['Internet_Users'] = df['Internet_Users'].str.replace(',', '', regex=False)
        df['Internet_Users'] = pd.to_numeric(df['Internet_Users'], errors='coerce')

        df.dropna(inplace=True)

        df.to_csv(CSV_FILE_PATH, index=False, encoding='utf-8')

        print("-" * 50)
        print(f"Success! Data saved to: {CSV_FILE_PATH}")
        print("-" * 50)
        print(df.head())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_and_save_internet_data()