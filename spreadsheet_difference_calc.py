import streamlit as st
import pandas as pd

def calculate_differences(uploaded_file1, uploaded_file2):
    # Load the CSV files into pandas DataFrames
    df1 = pd.read_csv(uploaded_file1)
    df2 = pd.read_csv(uploaded_file2)

    # Merge the two DataFrames on the specified column
    merged_df = pd.merge(df1, df2, on=column_name, suffixes=('_1', '_2'))

    # Remove commas from specified columns and convert to numeric
    merged_df[column_sub+'_1'] = pd.to_numeric(merged_df[column_sub+'_1'].str.replace(',', ''), errors='coerce')
    merged_df[column_sub+'_2'] = pd.to_numeric(merged_df[column_sub+'_2'].str.replace(',', ''), errors='coerce')

    # Calculate the difference between specified columns
    merged_df[column_new] = merged_df[column_sub+'_1'] - merged_df[column_sub+'_2']

    # Filter out rows where there is no difference
    differences_df = merged_df[merged_df[column_new] != 0]


    # Save the result to a new CSV file
    differences_df.to_csv(file_name + ".csv", index=False)

    st.success("Differences saved to " + file_name + ".csv")

# Create the Streamlit app
st.title("CSV Difference Calculator")

st.text("Created by Jared Nicastro")

#File Preferences
column_name = st.text_input("What column would you like to merge?")
column_sub = st.text_input("Name of column you want to subtract:")
column_new = st.text_input("Name of new column you want to create:")

# File upload
uploaded_file1 = st.file_uploader("Upload CSV file 1", type=["csv"])
uploaded_file2 = st.file_uploader("Upload CSV file 2", type=["csv"])
file_name = st.text_input("What would you like the name of your new spreadsheet to be?")

if uploaded_file1 and uploaded_file2 and file_name :
    # Calculate differences when both files are uploaded
    calculate_differences(uploaded_file1, uploaded_file2)