import streamlit as st
import psycopg2

# Database connection parameters
db_host = "postgres-db"  # PostgreSQL container name
db_name = "book_inventory"
db_user = "admin_user"
db_pass = "securepassword"

# Establish connection to PostgreSQL
conn = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=db_pass)
cursor = conn.cursor()

# Execute a query to fetch book data
cursor.execute("SELECT * FROM books;")
book_records = cursor.fetchall()

# Display the book data using Streamlit
st.title("Book Inventory")
for record in book_records:
    st.write(record)

# Clean up the database connection
cursor.close()
conn.close()
