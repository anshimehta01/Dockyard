# 🎓 University Database Setup with Docker 🐳

Welcome to the **University Database Setup**! This project helps you deploy a **MySQL database** inside a Docker container to manage student enrollment records efficiently. 🚀

---
## 🔧 Prerequisites
Make sure you have the following installed:
✅ **Docker** – For running the MySQL container.
✅ **Basic SQL knowledge** – To interact with the database.
✅ **A terminal or command prompt** – For executing commands.

---
## 📂 Project Structure
The project consists of the following files:
- **database_students.sql** – Contains SQL commands to set up the database.
- **Dockerfile** – Instructions to build a MySQL image with the database setup.
- **README.md** – Documentation for setting up and using the project.

---
## 🏗️ Setting Up the Database
### 1️⃣ Build the Docker Image
Run the following command to create the Docker image:
```sh
docker build -t university-db .
```
This will create a MySQL image with the database initialization script.

### 2️⃣ Run the MySQL Container
Launch the container with this command:
```sh
docker run -d -p 3306:3306 --name university-container university-db
```
This will:
- Run the container in the background (`-d` flag).
- Map **port 3306** on the container to **port 3306** on the host (`-p 3306:3306`).
- Name the container `university-container`.

### 3️⃣ Access the MySQL Database
Connect to the MySQL database inside the running container:
```sh
docker exec -it university-container mysql -uadmin_user -psecurepass university_db
```
Enter the password `securepass` when prompted.

---
## 🗂️ Database Schema
Inside the `university_db`, there is a table named `enrolled_students`:

| Column       | Type           | Constraints         |
|-------------|---------------|---------------------|
| student_id  | INT           | PRIMARY KEY (Auto-Increment) |
| first_name  | VARCHAR(100)  | NOT NULL           |
| last_name   | VARCHAR(100)  | NOT NULL           |

### 🛠️ SQL Commands
Once inside MySQL, you can execute the following commands:
#### Show Databases
```sql
SHOW DATABASES;
```
#### Select the University Database
```sql
USE university_db;
```
#### Show Tables
```sql
SHOW TABLES;
```
#### View Student Data
```sql
SELECT * FROM enrolled_students;
```

---
## 📌 Sample Data
The initial database setup includes sample students:

| student_id | first_name | last_name |
|------------|-----------|-----------|
| 1          | Sophia    | Miller    |
| 2          | James     | Davis     |

You can add more records using:
```sql
INSERT INTO enrolled_students (first_name, last_name) VALUES ('Emily', 'Clark');
```

---
## 🎯 What’s Next?
- Modify the database schema as needed.
- Insert more student records.
- Connect this database to your applications.
- Experiment with database queries and optimizations.

🔗 Explore more: [Docker Documentation](https://docs.docker.com/) | [MySQL Docs](https://dev.mysql.com/doc/)

💡 Pro Tip: Use `docker logs university-container` to check logs if the database does not start correctly.

Happy coding! 💻🎉



