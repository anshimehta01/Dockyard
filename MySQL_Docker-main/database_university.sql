 Create a new database
CREATE DATABASE university_db;
USE university_db;

 Create a table for students
CREATE TABLE enrolled_students (
    student_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (student_id)
);

 Insert sample data
INSERT INTO enrolled_students (first_name, last_name)
VALUES ('Sophia', 'Miller'), ('James', 'Davis');
