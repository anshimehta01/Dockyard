# ⚙️ Dockyard: Docker Projects & Experiments 🐳🚢

Welcome to **Dockyard**, a curated collection of Docker experiments and projects built to explore the power of containerization in software development, databases, machine learning, and cloud deployments. Whether you're a beginner or an advanced user, you'll find something interesting here to play with!

---

## 📦 Projects & Experiments

Here’s what you’ll find in this repo:

### 🐣 Docker Hello World  
> A simple "Hello World" app to get started with Docker basics. Great for first-time users!

### 🔗 Docker Networking  
> Learn how Docker containers communicate using networks. Set up bridge, host, and overlay networks.

### 📁 Docker Volumes  
> Explore persistent storage with Docker Volumes. Mount and manage data seamlessly between containers.

### 🌐 Full-Stack Docker App  
> A complete web application with backend, frontend, and database—all containerized and connected.

### ⚙️ Minikube + K9s (Kubernetes)  
> Run a lightweight Kubernetes cluster using Minikube. Visualize and manage resources with K9s.

### 🐬 MySQL in Docker  
> Set up a MySQL database inside a container and learn how to connect and manage it.

### 🎨 Streamlit Docker App  
> Create interactive dashboards and visualizations using Streamlit, all within a Docker container.

### 🤖 ML Model Deployment  
> Package and deploy machine learning models in a containerized environment for consistency and scalability.

---

## 📚 Resources for You

These helped me a lot—and might help you too!

- 📖 [Docker Documentation](https://docs.docker.com/)
- 🎬 [Docker YouTube Series](https://www.youtube.com/results?search_query=docker+tutorial)
- 🧾 [Docker Cheat Sheet](https://dockerlabs.collabnix.com/docker/cheatsheet/)
- 📘 [Streamlit Docs](https://docs.streamlit.io/)
- ☁️ [AWS CLI Setup Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

---

## 🛠 Requirements

Make sure to have the following installed:

- ✅ Docker → `docker --version`
- ✅ Python (for Streamlit apps)
- ✅ AWS CLI (for cloud deployment)
- ✅ Minikube & kubectl (for Kubernetes experiments)

---

## 🚀 Getting Started

Here's a quick example to run one of the apps:

```bash
cd Streamlit-docker-app-main
docker build -t streamlit-app .
docker run -p 8501:8501 streamlit-app

🤝 Contributing
🐞 Found a bug? Open an issue

💡 Got an idea? Submit a pull request

📚 Want to help with docs? Go ahead!

✨ Final Note
Whether you're testing your first Dockerfile or deploying ML models in the cloud—this repo is your dockyard to learn, build, and ship containers with confidence.
Happy Docking! 🐳🚀
