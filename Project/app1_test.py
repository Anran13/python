import yfinance as yf
import os
from datetime import datetime
import pandas as pd


def download_data():
    """
    1. download yfinance stack data: 2330.TW, 2303.TW, 2454.TW, 2317.TW
    2. establish a file called data in this project; if exists, skip
    3. downloaded data sets whose filename are 2330_date.csv, 2303_date.csv, 2454_date.csv, 2317_date.csv, if exists, skip
    4. if the existed csv files are not the up-to-date csv file, then remove the old ones and download data sets again and save them
    """

    if not os.path.exists('data'):
        os.makedirs('data')

    today = datetime.now().strftime('%Y-%m-%d')
    if not os.path.exists(f'data/2330_{today}.csv'):
        tw2330 = yf.download('2330.TW', start='2000-01-01', end=today, auto_adjust=True)
        tw2330.to_csv(f'data/2330_{today}.csv')

    if not os.path.exists(f'data/2303_{today}.csv'):
        tw2303 = yf.download('2303.TW', start='2000-01-01', end=today, auto_adjust=True)
        tw2303.to_csv(f'data/2303_{today}.csv')

    if not os.path.exists(f'data/2454_{today}.csv'):
        tw2454 = yf.download('2454.TW', start='2000-01-01', end=today, auto_adjust=True)
        tw2454.to_csv(f'data/2454_{today}.csv')

    if not os.path.exists(f'data/2317_{today}.csv'):
        tw2317 = yf.download('2317.TW', start='2000-01-01', end=today, auto_adjust=True)
        tw2317.to_csv(f'data/2317_{today}.csv')

    # Remove old files
    for stock_id in ['2330', '2303', '2454', '2317']:
        for filename in os.listdir('data'):
            if filename.startswith(f'{stock_id}_') and not filename.endswith(f'_{today}.csv'):
                os.remove(os.path.join('data', filename))


def combine_close_prices():
    """
    1. we already have the exist stack data in the data folder
    2. we need to combine the close prices of the four stocks into a single dataframe:
       the column names for date, 2330, 2303, 2454, 2317 are "date", "tsmc", "umc", "mediatec", and "honhai", respectively,
       and each rows are the ordered date of the close price of the four stocks
    """    
  
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Define a dictionary to map stock IDs to desired column names
    stock_names = {
        '2330': 'tsmc',
        '2303': 'umc',
        '2454': 'mediatec',
        '2317': 'honhai'
    }

    combined_df = pd.DataFrame()

    for stock_id, col_name in stock_names.items():
        filepath = os.path.join('data/', f'{stock_id}_{today}.csv')
        if os.path.exists(filepath):
            df = pd.read_csv(filepath, skiprows=2)
            df.columns = ['Date','Close','High','Low','Open','Volume']
            df.set_index('Date', inplace=True)
            df.index = pd.to_datetime(df.index)

            # Select only the 'Close' price and rename the column
            close_prices = df[['Close']].rename(columns={'Close': col_name})
            
            if combined_df.empty:
                combined_df = close_prices
            else:
                combined_df = combined_df.join(close_prices, how='outer')
        else:
            print(f"Warning: Data file for {stock_id} ({filepath}) not found. Skipping.")

    # Reset index to make 'Date' a column and rename it to 'date'
    combined_df = combined_df.reset_index().rename(columns={'Date': 'date'})
    return combined_df
     



def main():
    download_data()
    close_prices = combine_close_prices()
    print(close_prices)



if __name__ == "__main__":
    main()