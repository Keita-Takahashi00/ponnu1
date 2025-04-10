import streamlit as st
import pandas as pd

# List of CSV files
files = ["dm", "ds", "se", "sv"]

# Dictionary to store DataFrames
dataframes = {}

# Iterate through the list of files
for file in files:
    # Create a DataFrame and store it in the dictionary
    dataframes[file] = pd.read_csv(file + ".csv")

    # Display the DataFrame with a title
    st.markdown(f"## - _{file.upper()} domain_")
    st.write(dataframes[file])

# Use the 'sv' DataFrame from the dictionary
sv = dataframes["sv"]

# Create a new DataFrame with selected columns and rename 'sestdtc' to 'date'
df = sv[['usubjid', 'visit', 'sestdtc']].rename(columns={'sestdtc': 'date'})

# Convert 'date' column to numeric (YYYYMMDD format)
df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y%m%d').astype(float)

# Display the new DataFrame
st.markdown("## - _Filtered Data_")
st.write(df)
