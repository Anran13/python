import yfinance as yf
import os
from datetime import datetime
from pathlib import Path

def download_data():
    """
    Downloads and updates daily stock data for a predefined list of tickers.

    1.  Downloads data for: 2330.TW, 2303.TW, 2454.TW, 2317.TW.
    2.  Creates a 'data' directory if it doesn't exist.
    3.  For each stock, checks if a data file for the current date already exists.
    4.  If not, it downloads the new data, saves it, and then removes any older
        data files for that specific stock.
    """
    # --- Configuration ---
    DATA_DIR = Path("data")
    STOCK_LIST = ["2330.TW", "2303.TW", "2454.TW", "2317.TW"]
    START_DATE = "2000-01-01"
    # ---------------------

    # 1. Ensure the data directory exists
    DATA_DIR.mkdir(exist_ok=True)

    today_str = datetime.now().strftime('%Y-%m-%d')

    # 2. Loop through each stock
    for ticker in STOCK_LIST:
        stock_id = ticker.split('.')[0]
        today_filename = f"{stock_id}_{today_str}.csv"
        today_filepath = DATA_DIR / today_filename

        # 3. Check if today's file already exists
        if today_filepath.exists():
            print(f"Data for {ticker} ({today_filename}) is already up-to-date. Skipping.")
            continue

        print(f"Downloading data for {ticker}...")
        try:
            # 4. Download new data
            stock_data = yf.download(ticker, start=START_DATE, end=today_str, auto_adjust=True)

            # 5. Proceed only if download was successful and returned data
            if stock_data.empty:
                print(f"Warning: No data downloaded for {ticker}. It might be a holiday or an issue with the ticker.")
                continue
            
            # 6. Save the new file first to ensure data integrity
            stock_data.to_csv(today_filepath)
            print(f"Successfully saved new data to {today_filepath}")

            # 7. Then, remove old files for this specific stock
            for old_file in DATA_DIR.glob(f"{stock_id}_*.csv"):
                if old_file.name != today_filename:
                    print(f"Removing old file: {old_file}")
                    os.remove(old_file)

        except Exception as e:
            print(f"An error occurred while processing {ticker}: {e}")



def main():
    download_data()


if __name__ == "__main__":
    main()