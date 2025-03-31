🚀 Deploying a Full-Stack App with Docker

# 🚀 Deploying a Library Management System with Docker

## Introduction 🐳🌐

In this guide, we’ll containerize and deploy a **library management system** using **Docker**. Our setup includes a **Streamlit frontend** and a **PostgreSQL database backend**, both running in separate Docker containers. These containers will communicate seamlessly through a custom Docker network, making deployment effortless.

By the end of this tutorial, you'll have a fully functional library management system running in isolated containers—ready for development or production! 🚀

---

## 🏗️ Project Architecture

Our application consists of:
1. **PostgreSQL Database**: A containerized database for managing book records efficiently.
2. **Streamlit Frontend**: A lightweight, interactive web app to visualize and interact with the library data.

Both containers will be linked via a **custom Docker network** to ensure smooth communication.

---

## 📚 Prerequisites

Before diving in, ensure you have the following installed:

- **Docker**: The core tool for containerizing applications.
- **Docker Desktop**: A handy UI tool to manage containers locally.

---

## 🌐 Step 1: Create a Custom Docker Network

To enable communication between our containers, let's create a dedicated **Docker network**:

```bash
docker network create library_network

This network acts as a bridge, allowing the Streamlit app to interact with the PostgreSQL database.

🗄️ Step 2: Set Up the PostgreSQL Database
We’ll now launch our database container using the official PostgreSQL image.

docker run -d \  
  --name pg_container \  
  --network library_network \  
  -e POSTGRES_USER=lib_admin \  
  -e POSTGRES_PASSWORD=securepassword \  
  -e POSTGRES_DB=library_db \  
  postgres

🐍 Step 3: Build the Streamlit App Container
3.1 Create a Dockerfile for Streamlit
Inside your project folder, create a Dockerfile:

FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

3.2 Add Dependencies
Create a requirements.txt file:

streamlit
psycopg2-binary

3.3 Build the Streamlit Image
Run the following command to build the image:

docker build -t library_app .

3.4 Launch the Streamlit App Container
Now, let’s start the Streamlit app and connect it to our network:

docker run -d \  
  --name streamlit_ui \  
  --network library_network \  
  -p 8501:8501 \  
  library_app

This binds Streamlit to localhost:8501, making it accessible via a web browser.

🔗 Step 4: Connect Streamlit to PostgreSQL
4.1 Create the App File (main.py)
Inside your Streamlit project folder, create main.py:

import streamlit as st
import psycopg2

# Establish database connection
conn = psycopg2.connect(
    dbname="library_db",
    user="lib_admin",
    password="securepassword",
    host="pg_container",  # Referencing the PostgreSQL container
    port="5432"
)
cur = conn.cursor()

cur.execute("SELECT version();")
db_version = cur.fetchone()

st.title("Library Management System")
st.write("Connected to database:", db_version)

cur.close()
conn.close()

4.2 Test the Connection
Open your browser and visit:

http://localhost:8501

📊 Step 5: Insert and Retrieve Data

5.1 Access the PostgreSQL Container
To interact with the database directly, run:

docker exec -it pg_container psql -U lib_admin -d library_db

5.2 Create a Sample Table & Insert Data
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(100),
    published_year INT
);

INSERT INTO books (title, author, published_year) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', 1925),
('To Kill a Mockingbird', 'Harper Lee', 1960),
('1984', 'George Orwell', 1949);

SELECT * FROM books;

🚀 Step 6: Run the Full Application
docker run --name streamlit_ui --network library_network -p 8501:8501 library_app

🎉 Conclusion
Congratulations! 🎊 You’ve successfully built and deployed a fully containerized library management system using Docker. With this setup, your app is portable, scalable, and independent of the underlying system.

Keep exploring, experimenting, and pushing your projects further! 🚀🐳

Happy coding! 💻✨