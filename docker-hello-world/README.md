# Docker Basics: Hello World Project \U0001F433\U0001F40D

## Introduction
This project demonstrates the basics of Docker by creating and running a simple Python application inside a Docker container. The application prints `Hello World! \U0001F433` to the console when executed.

## Prerequisites \U0001F4CB
Before starting, ensure you have the following installed on your system:
- **Docker**: A platform for developing, shipping, and running applications in containers.
- **Python**: Required to write the application script.
- **Docker Desktop**: Helps manage Docker containers on your local machine.

## Step 1: Create the Python Application \U0001F40D
1. Open a terminal or PowerShell.
2. Navigate to your desired project directory.
3. Create a new Python file named `app.py` and add the following code:

    ```python
    # app.py
    print("Hello World! \U0001F433")
    ```

## Step 2: Install Docker and Python \U0001F6E0️
- **Install Docker**: Download and install Docker Desktop from the [official Docker website](https://www.docker.com/get-started).
- **Install Python**: Download and install Python from the [official Python website](https://www.python.org/downloads/).

## Step 3: Verify Installations ✅
Check if Docker and Python are installed correctly:

```sh
# Verify Docker installation
docker --version
```
Expected output:
```
Docker version XX.XX.XX, build XXXXXXX
```

```sh
# Verify Python installation
python --version
```
Expected output:
```
Python 3.X.X
```

## Step 4: Create a Dockerfile \U0001F4C4
Create a new file named `Dockerfile` (without an extension) in the same directory as `app.py` and add the following content:

```dockerfile
# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Run the Python script
CMD ["python", "app.py"]
```

## Step 5: Build the Docker Image \U0001F3D7️
Run the following command in your terminal to build the Docker image:

```sh
docker build -t hello-world-app .
```

- `-t hello-world-app`: Tags the image with the name `hello-world-app`.
- `.`: Specifies the build context (current directory).

## Step 6: Verify the Docker Image \U0001F5BC️
Check if the image was built successfully:

```sh
docker images
```
Expected output:
```
REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
hello-world-app     latest    abc123def456   A few seconds ago   XXMB
```

## Step 7: Run the Docker Container \U0001F680
Now, run the container using:

```sh
docker run hello-world-app
```
Expected output:
```
Hello World! \U0001F433
```

## Troubleshooting \U0001F527
If you encounter encoding errors like `SyntaxError: Non-UTF-8 code`, run the following command to fix the encoding:

```sh
Get-Content app.py | Set-Content -Encoding utf8 app.py
```

## Conclusion \U0001F389
Congratulations! \U0001F389 You have successfully created and executed a Dockerized Python application. This marks the beginning of your journey with Docker. Continue exploring more complex applications and Docker features!

### Useful Links
- [Docker Documentation](https://docs.docker.com/)
- [Python Official Website](https://www.python.org/)
- [DockerHub](https://hub.docker.com/)

