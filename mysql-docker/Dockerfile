# Use MySQL official image
FROM mysql:latest

# Set MySQL root password
ENV MYSQL_ROOT_PASSWORD=root

# Copy SQL script to auto-run
COPY ./database_students.sql /docker-entrypoint-initdb.d/
