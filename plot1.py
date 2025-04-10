import streamlit as st
import pandas as pd

# List of CSV files
csv_files = ["dm.csv", "ds.csv", "se.csv", "sv.csv"]

# Iterate through the list of files
for csv_file in csv_files:
    # Create a DataFrame
    df = pd.read_csv(csv_file)

    # Display the DataFrame with a title
    st.markdown(f"## - _{csv_file.split('.')[0].upper()} domain_")
    st.write(df)

# Create a new DataFrame with selected columns and rename 'sestdtc' to 'date'
df = sv_df[['usubjid', 'visit', 'sestdtc']].rename(columns={'sestdtc': 'date'})

# Convert 'date' column to numeric (YYYYMMDD format)
df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y%m%d').astype(float)

# Display the new DataFrame
print(df)
