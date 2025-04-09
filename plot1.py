import streamlit as st
import pandas as pd

# Load the CSV file
csv_file = "./dm.csv"

# Create a DataFrame
df = pd.read_csv(csv_file)

# Display the DataFrame
st.markdown("## - _DM domain_")
st.write(df)
