Streamlit Application with Docker

Overview

This project demonstrates how to containerize a Streamlit application using Docker. The application can be built and run inside a Docker container, making it easy to deploy on different systems.

Prerequisites

Ensure you have the following installed:

Python 3.9+

Docker

Project Structure

Streamlit_Docker/
│── Dockerfile
│── requirements.txt
│── Streamlit_app.py

Setup Instructions

1. Clone the Repository

git clone <repository_url>
cd Streamlit_Docker

2. Build the Docker Image

Run the following command to build the Docker image:

docker build -t streamlit_app .

3. Run the Container

Once the build is successful, run the container:

docker run -p 8501:8501 streamlit_app

4. Access the Application

Open your browser and go to:

http://localhost:8501

Dockerfile

# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . /app

# Install dependencies
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "Streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]

Troubleshooting

1. Docker Not Running

Ensure Docker is running before building the image:

docker ps

2. Connection Timeout during Build

If you face issues while installing dependencies, try using an alternative PyPI mirror:

RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt -i https://pypi.org/simple/

3. Port Already in Use

If port 8501 is already in use, change it in the run command:

docker run -p 8600:8501 streamlit_app

Then access it at:

http://localhost:8600

License

This project is open-source under the MIT License.

