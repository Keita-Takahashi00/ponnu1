import streamlit as st
import pandas as pd
import subprocess
import sys

# Ensure Plotly is installed
try:
    import plotly
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "plotly"])

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

# Explicitly create separate DataFrame variables
dm_df = dataframes["dm"]
ds_df = dataframes["ds"]
se_df = dataframes["se"]
sv_df = dataframes["sv"]

# Example: Display the dm_df DataFrame in the Streamlit app
#st.markdown("## - _DM DataFrame_")
st.write(sv_df)

# Create a new DataFrame with selected columns and rename 'sestdtc' to 'date'
vsdf = sv_df[['USUBJID', 'VISIT', 'SVSTDTC']].rename(columns={'SVSTDTC': 'DATE', 'VISIT': 'TEXT'})

# Convert 'date' column to numeric (YYYYMMDD format)
vsdf['DATE'] = pd.to_datetime(vsdf['DATE'], errors='coerce').dt.strftime('%Y%m%d').astype(float)

# Example: Display the dm_df DataFrame in the Streamlit app
st.markdown("## - _DataFrame_")
st.write(vsdf)

import plotly.express as px
# Streamlit app
st.title("Visualization of Subjects Over Time")

# Allow user to filter by subject (USUBJID)
selected_subjects = st.multiselect("Select Subjects (USUBJID):", options=vsdf['USUBJID'].unique(), default=vsdf['USUBJID'].unique())

# Filter data based on selected subjects
filtered_vsdf = vsdf[vsdf['USUBJID'].isin(selected_subjects)]

# Create scatter plot with Plotly
fig = px.scatter(
    filtered_vsdf,
    x='DATE',
    y='USUBJID',
    text='TEXT',
    title="Visualization of Subjects Over Time",
    labels={"USUBJID": "Subjects", "DATE": "Date"},
    template="plotly_white"
)

# Display text labels on the scatter plot
fig.update_traces(textposition='top center')

# Add x-axis and y-axis titles
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Subjects",
    showlegend=False
)

# Display the plot in Streamlit
st.plotly_chart(fig)

# Display the filtered DataFrame
st.markdown("### Filtered Data")
st.dataframe(filtered_vsdf)
