# type in terminal: streamlit run pandas2_4.py
import yfinance as yf
import os
from datetime import datetime
import pandas as pd
import streamlit as st
import glob

# --- 組態設定 (Configuration) ---
DATA_DIR = 'data'
STOCK_MAPPING = {
    '2330.TW': 'tsmc',
    '2303.TW': 'umc',
    '2454.TW': 'mediatec',
    '2317.TW': 'honhai'
}

# --- 資料處理函式 ---
def download_data():
    """
    下載並儲存指定股票的最新資料。
    - 如果 'data' 資料夾不存在，則建立它。
    - 下載從 2000-01-01 到今天的資料。
    - 如果當天的檔案已存在，則跳過下載。
    - 移除舊的資料檔，保持資料夾整潔。
    """
    os.makedirs(DATA_DIR, exist_ok=True)
    today_str = datetime.now().strftime('%Y-%m-%d')

    for ticker in STOCK_MAPPING.keys():
        stock_id = ticker.split('.')[0]
        
        # 清理此股票的舊檔案
        for filename in glob.glob(os.path.join(DATA_DIR, f'{stock_id}_*.csv')):
            if not filename.endswith(f'_{today_str}.csv'):
                os.remove(filename)
                st.info(f"已移除舊資料檔: {filename}")

        # 如果今日檔案不存在，則下載新資料
        filepath = os.path.join(DATA_DIR, f'{stock_id}_{today_str}.csv')
        if not os.path.exists(filepath):
            with st.spinner(f'正在下載 {ticker} 的最新資料...'):
                data = yf.download(ticker, start='2000-01-01', end=today_str, auto_adjust=True)
                if not data.empty:
                    data.to_csv(filepath)
                    st.success(f"已成功下載 {ticker} 的資料")
                else:
                    st.warning(f"無法下載 {ticker} 的資料")

@st.cache_data
def load_combined_data():
    """
    為每支股票載入最新的 CSV 檔案，合併其 'Close' (收盤價) 欄位，
    並返回一個單一的 DataFrame。
    
    Returns:
        pd.DataFrame: 一個以日期為索引，並包含每支股票收盤價欄位的 DataFrame。
                      如果找不到任何資料檔，則返回一個空的 DataFrame。
    """
    all_close_prices = []
    
    for ticker, name in STOCK_MAPPING.items():
        stock_id = ticker.split('.')[0]
        
        # 尋找該股票最新的檔案
        try:
            list_of_files = glob.glob(os.path.join(DATA_DIR, f'{stock_id}_*.csv'))
            if not list_of_files:
                st.warning(f"找不到 {name} ({stock_id}) 的資料檔，請先點擊更新按鈕。")
                continue
            
            latest_file = max(list_of_files, key=os.path.getctime)
            
            # 讀取 CSV，只選擇需要的欄位以提升效率
            # df = pd.read_csv(
            #     latest_file, 
            #     usecols=['Date', 'Close'],
            #     index_col='Date',
            #     parse_dates=True
            # ).rename(columns={'Close': name})

            df = pd.read_csv(latest_file, skiprows=2)
            df.columns = ['Date','Close','High','Low','Open','Volume']
            df.set_index('Date', inplace=True)
            df.index = pd.to_datetime(df.index)
            df = df[['Close']].rename(columns={'Close': name})

            
            all_close_prices.append(df)
        except Exception as e:
            st.error(f"讀取 {name} ({stock_id}) 的檔案時發生錯誤: {e}")

    if not all_close_prices:
        return pd.DataFrame()

    # 一次性合併所有 DataFrame，並按日期排序
    combined_df = pd.concat(all_close_prices, axis=1).sort_index()
    return combined_df

# --- Streamlit 介面 ---
def main():
    st.title('台灣主要科技股股價趨勢圖')

    st.sidebar.header('控制選項')
    if st.sidebar.button('更新最新股價資料'):
        download_data()
        st.cache_data.clear() # 清除快取以重新載入資料

    data = load_combined_data()

    if data.empty:
        st.warning("請先點擊側邊欄的按鈕來下載或更新資料。")
        return

    stock_options = list(STOCK_MAPPING.values())
    selected_stocks = st.sidebar.multiselect('選擇股票:', stock_options, default=stock_options[:2])

    start_date = st.sidebar.date_input('開始日期', data.index.min().date())
    end_date = st.sidebar.date_input('結束日期', data.index.max().date())

    if selected_stocks:
        # 根據選擇的日期和股票篩選資料
        filtered_data = data.loc[start_date:end_date, selected_stocks]
        
        st.header('股價走勢')
        st.line_chart(filtered_data)

        if st.checkbox('顯示原始資料'):
            st.dataframe(filtered_data)
    else:
        st.warning('請至少選擇一支股票。')

if __name__ == "__main__":
    main()