# Use the official MySQL image
FROM mysql:latest

# Set environment variables
ENV MYSQL_DATABASE=university_db
ENV MYSQL_USER=admin_user
ENV MYSQL_PASSWORD=securepass
ENV MYSQL_ROOT_PASSWORD=rootpass

# Copy the modified SQL script to the container
COPY database_students.sql /docker-entrypoint-initdb.d/init.sql

# Expose MySQL port
EXPOSE 3306
