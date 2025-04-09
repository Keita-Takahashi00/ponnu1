pip install streamlit as st
pip install pandas as pd

# Load the JSON file
json_file = "./dm.json"

# Create a DataFrame
df = pd.read_json(json_file)

# Display the DataFrame
print(df)
