# Use official Python as base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the files to the container
COPY . /app

# Install dependencies
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt


# Expose port 8501 for Streamlit
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
