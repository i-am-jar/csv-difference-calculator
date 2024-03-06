# Use an official Python runtime as the base image
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port that Streamlit runs on
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Set the command to run the Streamlit application
ENTRYPOINT ["streamlit", "run", "spreadsheet_difference_calc.py", "--server.port=8501"]