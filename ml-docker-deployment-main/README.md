Deploying a Machine Learning Model with Docker 🚀🤖

Welcome to this hands-on guide for deploying a Machine Learning (ML) model using Docker! In this project, we will containerize an ML model and serve it as a Streamlit web application, making it accessible and scalable across different environments.

🌟 Why Use Docker for ML Deployment?

Portability 📦: Run your ML model anywhere, independent of the system.

Scalability 📈: Deploy and scale effortlessly with containers.

Reproducibility 🔁: Ensures consistent performance across environments.

📌 Prerequisites

Before you begin, make sure you have the following installed:
✅ Docker – A tool for containerizing applications.
✅ Python – Programming language for ML development.
✅ Streamlit – A lightweight web framework for interactive applications.

🏗️ Project Setup

Step 1️⃣: Verify Docker and Python Installation

Check your Docker version:
docker --version

Check your Python version:
python3 --version

📂 Project Structure

Your project should have the following structure:
ml-docker-deployment/
├── app.py            # ML model and Streamlit app
├── requirements.txt  # Dependencies
├── Dockerfile        # Docker build instructions
├── mushrooms.csv     # Dataset
└── .dockerignore     # Excluded files for Docker build
🏗️ Building the ML Model and Streamlit App

Step 2️⃣: Write the ML Model in app.py
Create a Python script with data preprocessing, model training, and a Streamlit interface:
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.title("Mushroom Classification 🍄")

# Load dataset
df = pd.read_csv("mushrooms.csv")
X = df.drop(columns=['class'])
y = df['class']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

st.write("Model is trained and ready!")

Step 3️⃣: Create requirements.txt

List all required Python dependencies:
pip freeze > requirements.txt

Ensure it includes:
streamlit
pandas
scikit-learn

🐳 Dockerizing the ML Model

Step 4️⃣: Create a Dockerfile
# Use Python 3.9 slim as base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Streamlit
EXPOSE 8501

# Run Streamlit app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

🚀 Running the Dockerized ML Model

Step 5️⃣: Build the Docker Image
docker build -t ml-model .
Verify the image:
docker images

Step 6️⃣: Run the Docker Container
docker run -p 8501:8501 ml-model

🐋 Pushing the Docker Image to DockerHub

Step 7️⃣: Log in to DockerHub
docker login

Step 8️⃣: Tag the Docker Image
docker tag ml-model yourdockerhubusername/ml-model

Step 9️⃣: Push the Docker Image
docker push yourdockerhubusername/ml-model

🎉 Conclusion

Congratulations! 🎉 You have successfully:
✅ Built a Machine Learning model
✅ Containerized it using Docker
✅ Deployed it as a web app
