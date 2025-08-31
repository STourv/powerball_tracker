import pandas as pd
from datetime import datetime
import requests

# -------------------------
# Fetch the last 30 Powerball draws
# -------------------------

# Example public data source (NY Powerball JSON)
URL = "https://data.ny.gov/resource/d6yy-54nr.json?$limit=30&$order=draw_date DESC"

def fetch_powerball_draws():
    response = requests.get(URL)
    response.raise_for_status()  # Raise error if request fails
    data = response.json()

    # Create DataFrame
    df = pd.DataFrame(data)

    # Convert date strings to datetime objects
    df['draw_date'] = pd.to_datetime(df['draw_date']).dt.date

    # Rename columns for clarity
    df.rename(columns={
        'draw_date': 'Draw Date',
        'winning_numbers': 'Winning Numbers',
        'multiplier': 'Multiplier'
    }, inplace=True)

    # Keep only relevant columns
    return df[['Draw Date', 'Winning Numbers', 'Multiplier']]

# -------------------------
# Save draws to Excel
# -------------------------
def save_to_excel(df, filename="powerball_draws.xlsx"):
    df.to_excel(filename, index=False)
    print(f"✅ Saved {len(df)} draws to {filename}")

# -------------------------
# Main script
# -------------------------
if __name__ == "__main__":
    print("Fetching latest Powerball draws...")
    df = fetch_powerball_draws()
    save_to_excel(df)
