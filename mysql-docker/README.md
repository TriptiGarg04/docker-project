# Running MySQL Using Docker 🐳📊

This project demonstrates how to containerize a **MySQL database** using **Docker**. The database is initialized with a sample schema and data, allowing you to interact with it using SQL queries.

## 📖 Project Overview
We will:
1. **Deploy** MySQL inside a Docker container.
2. **Initialize** the database with a sample dataset.
3. **Interact** with the database using SQL queries.

## 📋 Prerequisites
Ensure you have the following installed:
- **Docker**: A platform to develop, ship, and run applications in containers.
- **Docker Desktop**: A tool to manage Docker containers on your local machine.

## 🛠️ Installation and Setup

### Step 1: Verify Docker Installation
Run:
```sh
docker --version
```
Example output:
```sh
Docker version 20.10.17, build 100c701
```

### Step 2: Create the Project Files
#### **1. Create `database_students.sql`**
```sql
CREATE DATABASE student;
USE student;

CREATE TABLE students (
    StudentID INT NOT NULL AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    Surname VARCHAR(100) NOT NULL,
    PRIMARY KEY (StudentID)
);

INSERT INTO students (FirstName, Surname)
VALUES ("John", "Andersen"), ("Emma", "Smith");
```

#### **2. Create `Dockerfile`**
```Dockerfile
# Use the official MySQL image
FROM mysql:latest

# Set the root password for MySQL
ENV MYSQL_ROOT_PASSWORD=root

# Copy the SQL script to initialize the database
COPY ./database_students.sql /docker-entrypoint-initdb.d/
```

## 🚀 Deployment

### Step 1: Build the Docker Image
```sh
docker build -t mysql_db .
```

### Step 2: Verify the Docker Image
```sh
docker images
```
Example output:
```
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
mysql_db     latest    abc123def456   10 seconds ago   500MB
```

### Step 3: Run the Docker Container
```sh
docker run -d --name mysql_container mysql_db
```

### Step 4: Access the MySQL Container
```sh
docker exec -it mysql_container mysql -u root -p
```
(Enter password: `root` when prompted)

### Step 5: Verify the Database
```sql
SHOW DATABASES;
USE student;
SHOW TABLES;
SELECT * FROM students;
```
Expected Output:
```
+-----------+-----------+----------+
| StudentID | FirstName | Surname  |
+-----------+-----------+----------+
|         1 | John      | Andersen |
|         2 | Emma      | Smith    |
+-----------+-----------+----------+
```

## 🎉 Conclusion
You have successfully deployed a **MySQL database** using **Docker**! 🚀

✅ **Key Benefits:**
- **Portable & Scalable** database setup.
- **Easy to replicate** for development or testing.
- **Works on any system** with Docker installed.

💻 **Happy coding!** 😊

