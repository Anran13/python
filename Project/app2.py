import requests
from io import StringIO
from csv import DictReader
from requests import RequestException, HTTPError
import streamlit as st
import pandas as pd


@st.cache_data # temporal data used
def get_youbikes()->list:
    url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?page=0&size=1000'
    try:
        r = requests.request('GET', url)
        r.raise_for_status()     

    # check: if the HTTP request returned an unsuccessful status code.
    except HTTPError as e:
        raise Exception("Server problem!")
    # check all: all exceptions
    except RequestException as e:
        raise Exception("Connection problem!")

    else:
        print("Download successfully!")
        file = StringIO(r.text)
        list_reader = list(DictReader(file))
        return list_reader
    

st.title("Taipei YouBike Real-time Data")

# Use session state to store the data once fetched to avoid re-fetching on every interaction.
if 'data' not in st.session_state:
    st.session_state.data = None

# The button to fetch or refresh the data.
if st.button("Fetch/Refresh YouBike Data"):
    with st.spinner("Fetching data from the server..."):
        try:
            # Fetch data and store it in session state
            st.session_state.data = get_youbikes()
            st.success("Data fetched successfully!")
        except Exception as e:
            st.error(f"Failed to fetch data: {e}")
            st.session_state.data = None # Clear data on error

# Only display the panels if data has been successfully fetched.
if st.session_state.data:
    # Convert list of dicts to a pandas DataFrame for easier manipulation
    df = pd.DataFrame(st.session_state.data)
    
    # Data cleaning for map: ensure lat/lng are numeric and not null
    df['lat'] = pd.to_numeric(df['lat'], errors='coerce')
    df['lng'] = pd.to_numeric(df['lng'], errors='coerce')
    df.dropna(subset=['lat', 'lng'], inplace=True)

    # --- 1. Left panel: Sidebar for filtering ---
    with st.sidebar:
        st.header("Filter Options")
        # Get unique areas from the 'sarea' column and add an 'All' option
        areas = sorted(df['sarea'].unique())
        areas.insert(0, "All Areas")
        
        selected_area = st.selectbox(
            "Choose a station area:",
            options=areas
        )

    # --- 2. Right panel: Dataframe display ---
    st.header(f"Displaying Stations in: {selected_area}")

    filtered_df = df if selected_area == "All Areas" else df[df['sarea'] == selected_area]

    st.dataframe(filtered_df)

    # --- 3. Bottom panel: Map display ---
    st.header("Station Map")
    
    # st.map requires 'lat' and 'lon' columns. The source data has 'lat' and 'lng'.
    map_df = filtered_df.copy().rename(columns={'lng': 'lon'})
    if not map_df.empty:
        st.map(map_df)
    else:
        st.warning("No data to display on the map for the selected area.")
else:
    st.info("Click the button above to fetch and display YouBike data.")