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

import matplotlib.pyplot as plt

# Streamlit app
st.title("Visualization of Subjects Over Time")

# Allow user to filter by subject (USUBJID)
selected_subjects = st.multiselect("Select Subjects (USUBJID):", options=vsdf['USUBJID'].unique(), default=vsdf['USUBJID'].unique())

# Filter data based on selected subjects
filtered_vsdf = vsdf[vsdf['USUBJID'].isin(selected_subjects)]

# Create a scatter plot using Matplotlib
fig, ax = plt.subplots(figsize=(10, 6))

# Plot data for each subject
for subject in filtered_vsdf['USUBJID'].unique():
    subject_data = filtered_vsdf[filtered_vsdf['USUBJID'] == subject]
    ax.scatter(subject_data['DATE'], [subject] * len(subject_data), label=subject)
    for _, row in subject_data.iterrows():
        ax.text(row['DATE'], subject, row['TEXT'], fontsize=9, ha='right')

# Customize the plot
ax.set_title("Subjects Over Time", fontsize=16)
ax.set_xlabel("Date", fontsize=14)
ax.set_ylabel("Subjects (USUBJID)", fontsize=14)
ax.set_yticks(filtered_vsdf['USUBJID'].unique())
ax.grid(True)
ax.legend(title="Subjects", loc='upper left', bbox_to_anchor=(1, 1))

# Display the plot in Streamlit
st.pyplot(fig)

# Display the filtered DataFrame
st.markdown("### Filtered Data")
st.dataframe(filtered_vsdf)
