# Base image for Python applications
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy application files to the container
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the Streamlit application
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "stream.py", "--server.port=8501", "--server.address=0.0.0.0"]
