# This .py file has to be executed in the terminal (under the adequate filepath)
# In terminal --> enter "streamlit run _name_.py", i.e. "streamlit run test_streamlit.py"
# If we'd like to leave the page of Streamlit, press "Ctrl + C", 
# and go back to the web page and press "F5" to refresh the web page
# So, the terminal will not in execution.

# Show the "taiwan.csv" in the web page
import streamlit as st
import pandas as pd

def main():
    st.title("This is my first Streamlit App")
    st.write("Welcome to my Streamlit app！")
    
    # Load the CSV file
    df = pd.read_csv("taiwan.csv")
    
    # Display the DataFrame
    st.write("The following is the content of 'taiwan.csv'：")
    st.dataframe(df)

if __name__ == "__main__":
    main()