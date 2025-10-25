

---

````{"variant":"standard","title":"DevOps Assignment 2 README (Aashrith Sharma)","id":"58392"}
# DevOps Assignment 2 - Movie Ticket Booking Platform with CI/CD Pipeline

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-Latest-green)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI/CD-red?logo=jenkins&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Ready-326CE5)
![CI/CD](https://img.shields.io/badge/Jenkins-Pipeline-red)

A **production-ready Flask web application** for movie ticket booking integrated with a complete **CI/CD pipeline** using **Jenkins**, **Docker**, and **Kubernetes** for automated deployment and scalability.

---

## 🎯 Overview

This project demonstrates an end-to-end **DevOps workflow** for a Flask-based web application with:

- **Containerization** using Docker  
- **Automated CI/CD** using Jenkins pipelines  
- **Kubernetes orchestration** for scalable deployment  
- **Continuous testing and deployment** for reliability  

---

## 🌐 About the Web Application

The **Movie Ticket Booking Platform** allows users to:

- View currently running movies  
- Check showtimes and seat availability  
- Choose seats and book tickets  
- Make payments securely  

The platform is designed for **responsiveness**, **real-time seat updates**, and a **smooth user experience** across devices.

---

## ✨ Key Features

- **Flask Application** – Lightweight and modular backend  
- **Dockerized Deployment** – Multi-stage builds for optimized images  
- **Kubernetes Manifests** – Scalable pods and services for production use  
- **Jenkins CI/CD** – Automated pipeline for build, test, and deployment  
- **Docker Hub Integration** – Auto push/pull of images  
- **Health Checks & Monitoring** – Ensures application uptime  
- **Load Balancing** – Efficient traffic distribution via Kubernetes Service  

---

## 🏗️ System Architecture

```
             ┌──────────────────────────┐
             │      GitHub Repo          │
             │ aashrith/Movie-Ticket-App │
             └──────────┬────────────────┘
                        │
                        ▼
             ┌────────────────────┐
             │      Jenkins        │
             │   CI/CD Pipeline    │
             └──────────┬──────────┘
                        │
                        ▼
             ┌──────────────────────────┐
             │       Docker Hub         │
             │  aashrith/ticket-app     │
             └──────────┬───────────────┘
                        │
                        ▼
             ┌────────────────────┐
             │   Kubernetes        │
             │  Cluster (Pods)     │
             └──────────┬──────────┘
                        │
                        ▼
             ┌────────────────────┐
             │   LoadBalancer      │
             │   Service (External)│
             └──────────┬──────────┘
                        │
                        ▼
             ┌────────────────────┐
             │   End Users         │
             └────────────────────┘
```

---

## 📦 Prerequisites

- **Python 3.10+** → [Download](https://www.python.org/downloads/)  
- **Docker** → [Install](https://docs.docker.com/get-docker/)  
- **Kubernetes (kubectl)** → [Install](https://kubernetes.io/docs/tasks/tools/)  
- **Minikube** (for local testing) → [Install](https://minikube.sigs.k8s.io/docs/start/)  
- **Jenkins** → [Install](https://www.jenkins.io/doc/book/installing/)  
- **Git** → [Install](https://git-scm.com/downloads/)  

---

## 📁 Project Structure

```bash
DevOps-Assignment-2/
│
├── app.py                      # Flask application entry point
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker configuration
├── Jenkinsfile                  # CI/CD pipeline definition
├── README.md                    # Project documentation
├── .gitignore                   # Git ignore rules
├── .dockerignore                # Docker ignore rules
│
├── templates/                   # HTML templates
│   ├── index.html
│   ├── movies.html
│   ├── seat_selection.html
│   └── payment.html
│
├── static/                      # CSS, JS, and images
│   ├── css/
│   └── js/
│
├── k8s/                         # Kubernetes manifests
│   ├── deployment.yaml
│   └── service.yaml
│
└── screenshots/                 # Pipeline and deployment screenshots
```

---

## 🚀 Local Development

```bash
# Clone repository
git clone https://github.com/aashrith/Movie-Ticket-App.git
cd Movie-Ticket-App

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py
```

---

## 🐳 Docker Deployment

```bash
# Build Docker image
docker build -t aashrith/ticket-booking-flask:latest .

# Run container
docker run -d -p 5000:5000 aashrith/ticket-booking-flask:latest

# Stop and remove container
docker stop movie-app && docker rm movie-app
```

### Push to Docker Hub
```bash
docker tag movie-ticket-app aashrith/ticket-booking-flask:latest
docker login
docker push aashrith/ticket-booking-flask:latest
```

---

## ☸️ Kubernetes Deployment

```bash
# Start Minikube
minikube start

# Apply deployment files
kubectl apply -f k8s/

# Verify pods and services
kubectl get pods
kubectl get services
```

**Scale replicas:**
```bash
kubectl scale deployment ticket-booking-flask --replicas=3
```

**Delete deployment:**
```bash
kubectl delete -f k8s/
```

---

## 🔄 CI/CD Pipeline

### Stages

1. **Checkout Code** – Pulls the latest code from GitHub.  
2. **Build Docker Image** – Builds and tags image for Docker Hub.  
3. **Run Tests** – Executes basic health checks.  
4. **Push to Docker Hub** – Publishes image for deployment.  
5. **Deploy to Kubernetes** – Applies manifests and exposes service.  

---

### Jenkins Configuration

**Required Plugins:**
- Docker Pipeline  
- Kubernetes CLI  
- Git  

**Credentials Setup:**
- **Docker Hub** → `docker-hub-cred`  
- **Kubernetes Config** → `kubeconfig`  

**Pipeline Variables:**
```groovy
DOCKERHUB_CREDENTIALS = credentials('docker-hub-cred')
DOCKER_IMAGE = 'aashrith/ticket-booking-flask'
K8S_NAMESPACE = 'default'
```

**Steps:**
1. Create a new Jenkins pipeline job.  
2. Connect to your GitHub repo.  
3. Use the `Jenkinsfile` from the repository.  
4. Build and monitor from Jenkins Dashboard.  

---

## 👤 Author

**Name:** Aashrith Sharma  
**Roll Number:** 160122771053  

- **GitHub:** [github.com/aashrith](https://github.com/aashrith)  
- **Docker Hub:** [hub.docker.com/u/aashrith](https://hub.docker.com/u/aashrith)  

---

## 🙏 Acknowledgments

- Flask – Python web framework  
- Docker – Containerization  
- Jenkins – CI/CD automation  
- Kubernetes – Deployment and scaling  
````
