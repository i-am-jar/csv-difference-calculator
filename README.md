# CSV/Excel Operations Calculator

The CSV Difference Calculator is a Streamlit application designed to streamline the process of calculating differences between two CSV files. This tool is useful for users who need to compare data from different sources, identify discrepancies, and generate reports based on the differences.

## Features

- **Upload CSV/XLSX/XLS Files:** Users can upload two CSV files directly into the application.
- **Select Columns:** Users can select the columns to use for merging, subtraction, and creating a new column.
- **Automatic Calculation:** The application automatically calculates the differences between the uploaded CSV files when all necessary inputs are provided.
- **Seamless User Experience:** With a streamlined interface, users can initiate the calculation process effortlessly.

## Technologies Used

- Python
- Streamlit
- Pandas
- openpyxl

## Getting Started

To run the CSV/Excel Operations Calculator locally, follow these steps:

1. Clone this repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the application using `streamlit run spreadsheet_difference_calc.py`.

## How to Use

1. **Upload CSV/XLSX/XLS Files:** Click on the "Upload CSV file 1" and "Upload CSV file 2" buttons to upload your CSV files.
2. **Select Columns:** Choose the columns to use for merging, subtraction, and creating a new column from the dropdown menus.
3. **Provide Spreadsheet Name:** Enter the desired name for the new spreadsheet.
4. **Initiate Calculation:** The application automatically calculates the differences once all inputs are provided.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
