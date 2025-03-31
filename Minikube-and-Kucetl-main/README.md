# 🏗️ Minikube & kubectl: Kubernetes Local Setup Guide 🚀

This guide helps you set up **Minikube** and **kubectl** to run a Kubernetes cluster on your local machine. Minikube provides a lightweight Kubernetes environment, while kubectl is the command-line tool used to interact with Kubernetes resources.

---

## ✅ Prerequisites

Ensure you have:
- 🖥️ **Minikube Installed** – A local Kubernetes cluster manager.
- 🛠️ **kubectl Installed** – The command-line tool for managing Kubernetes.

---

## 🔧 Step 1: Install Minikube & kubectl

### Install Minikube:
- **Linux:**  
  ```sh
  curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
  ```
- **macOS:**  
  ```sh
  brew install minikube
  ```
- **Windows:** Install via Chocolatey:  
  ```sh
  choco install minikube
  ```

### Install kubectl:
- **Linux/macOS:**  
  ```sh
  curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl"
  ```
- **Windows:** [Download kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/)

---

## 🚀 Step 2: Start Your Minikube Cluster

Run the following command to start Minikube:
```sh
minikube start
```
This will initialize a local Kubernetes cluster.

To check if Minikube is running:
```sh
kubectl get nodes
```
Expected output:
```sh
NAME       STATUS   ROLES    AGE    VERSION
minikube   Ready    master   5m     v1.25.0
```

---

## 📦 Step 3: Deploy an Application

### 3.1 Create a Deployment
Deploy an **nginx** web server:
```sh
kubectl create deployment web-app --image=nginx
```

### 3.2 Expose the Deployment
Expose the application to the outside world:
```sh
kubectl expose deployment web-app --type=NodePort --port=80
```

### 3.3 Get Service URL
Retrieve the URL where your app is accessible:
```sh
minikube service web-app --url
```

---

## 📊 Step 4: Managing Your Kubernetes Cluster

### 4.1 Check Running Pods
```sh
kubectl get pods
```
Expected output:
```sh
NAME                        READY   STATUS    RESTARTS   AGE
web-app-65c8b9d88f-abc12    1/1     Running   0          3m
```

### 4.2 Scale the Deployment
Increase the number of running replicas:
```sh
kubectl scale deployment web-app --replicas=3
```
Verify scaling:
```sh
kubectl get pods
```

---

## 🔄 Step 5: Cleanup Resources
When you're done testing, delete the deployment and service:
```sh
kubectl delete service web-app
kubectl delete deployment web-app
```

To stop Minikube:
```sh
minikube stop
```

To delete the Minikube cluster:
```sh
minikube delete
```

---

## 🔍 Quick Kubernetes Command Recap:
```sh
# Start Minikube
minikube start

# Check Kubernetes cluster status
kubectl get nodes

# Deploy a sample application
kubectl create deployment web-app --image=nginx

# Expose the app via a NodePort
kubectl expose deployment web-app --type=NodePort --port=80

# Get the accessible URL
minikube service web-app --url

# List all running pods
kubectl get pods

# Scale the deployment to 3 replicas
kubectl scale deployment web-app --replicas=3

# Clean up resources
kubectl delete service web-app
kubectl delete deployment web-app
```

---

## 🎯 Conclusion
By using Minikube and kubectl, you can deploy and manage Kubernetes workloads locally. This setup is perfect for testing Kubernetes applications before moving to a production cluster.

🔗 **Next Steps:**
- Try different container images.
- Explore Kubernetes YAML manifests.
- Experiment with Helm charts for easier deployment.

🚀 Keep experimenting with Kubernetes! 🐳


