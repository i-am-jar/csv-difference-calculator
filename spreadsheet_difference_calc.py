import streamlit as st
import pandas as pd

def calculate_differences(df1, df2, column_name, column_sub, column_new, file_name):

    # Merge the two DataFrames on the specified column
    merged_df = pd.merge(df1, df2, on=column_name, suffixes=('_1', '_2'))

    # Remove commas from specified columns and convert to numeric
    merged_df[column_sub+'_1'] = pd.to_numeric(merged_df[column_sub+'_1'].str.replace(',', ''), errors='coerce')
    merged_df[column_sub+'_2'] = pd.to_numeric(merged_df[column_sub+'_2'].str.replace(',', ''), errors='coerce')

    # Calculate the difference between specified columns
    if operation == "Subtract":
        merged_df[column_new] = merged_df[column_sub+'_1'] - merged_df[column_sub+'_2']
    elif operation == "Add":
        merged_df[column_new] = merged_df[column_sub+'_1'] + merged_df[column_sub+'_2']
    elif operation == "Divide":
        merged_df[column_new] = merged_df[column_sub+'_1'] / merged_df[column_sub+'_2']
    elif operation == "Multiply":
        merged_df[column_new] = merged_df[column_sub+'_1'] * merged_df[column_sub+'_2']

    # Filter out rows where there is no difference
    differences_df = merged_df[merged_df[column_new] != 0]

    # Save the result to a new CSV file
    differences_df.to_csv(file_name + ".csv", index=False)

    st.success("Differences saved to " + file_name + ".csv")

    # Add a download button for the generated CSV file
    download_button_str = f"Download {file_name}.csv"
    st.download_button(label=download_button_str, data=differences_df.to_csv(), file_name=file_name + ".csv", mime='text/csv')

# Create the Streamlit app
st.title("CSV Difference Calculator")
st.text("Created by Jared Nicastro")

# File upload
uploaded_file1 = st.file_uploader("Upload CSV file 1", type=["csv"])
uploaded_file2 = st.file_uploader("Upload CSV file 2", type=["csv"])
file_name = st.text_input("What would you like the name of your new spreadsheet to be?")

# Check if both files have been uploaded
if uploaded_file1 and uploaded_file2 and file_name:
    # Read the CSV files into DataFrames
    df1 = pd.read_csv(uploaded_file1)
    df2 = pd.read_csv(uploaded_file2)

# Create dropdowns for column selection
    column_options = df1.columns.tolist()
    column_name = st.selectbox("Select column to merge:", column_options)
    column_sub = st.selectbox("Select column to perform operation:", column_options)
    column_new = st.text_input("Name of new column to create:")
    operation = st.radio("Select operation:", ["Add","Subtract", "Divide", "Multiply"])

if uploaded_file1 and uploaded_file2 and file_name and column_new :
    # Calculate differences when both files are uploaded
    calculate_differences(df1, df2, column_name, column_sub, column_new, file_name)
