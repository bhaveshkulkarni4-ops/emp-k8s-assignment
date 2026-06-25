# Employee Management Application on Google Kubernetes Engine (GKE)

## Assignment Details

**Assignment:** Kubernetes and DevOps Advance + FinOps (Cloud)

**Prepared By:** Bhavesh Kulkarni

**Employee ID:** 3175273

---

# Project Overview

This project demonstrates the deployment of a Dockerized Employee Management Application on Google Kubernetes Engine (GKE) using Kubernetes best practices. The application is deployed with high availability, persistent storage, secure configuration management, external access through Ingress, and automatic scaling using Horizontal Pod Autoscaler (HPA).

---

# Repository Details

## GitHub Repository

https://github.com/bhaveshkulkarni4-ops/emp-k8s-assignment

## Docker Hub Repository

[https://hub.docker.com/r/bhaveshkulkarni4/employee-app](https://hub.docker.com/repository/docker/bhaveshkulkarni4/employee-app/general)

**Docker Image**

bhaveshkulkarni4/employee-app:v1

---

# Technology Stack

- Python Flask
- MySQL 8.0
- Docker
- Docker Hub
- Kubernetes
- Google Kubernetes Engine (GKE)
- GitHub

---

# Project Structure

```
emp-k8s-assignment/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
│
└── k8s/
    ├── deployment.yaml
    ├── service.yaml
    ├── ingress.yaml
    ├── statefulset.yaml
    ├── configmap.yaml
    ├── secret.yaml
    ├── pvc.yaml
    └── hpa.yaml
```

---

# Kubernetes Resources Implemented

- Deployment
- StatefulSet
- Service
- Ingress
- ConfigMap
- Secret
- Persistent Volume Claim (PVC)
- Horizontal Pod Autoscaler (HPA)

---

# Deployment Steps

## 1. Build Docker Image

```bash
docker build -t employee-app:v1 .
```

## 2. Tag Docker Image

```bash
docker tag employee-app:v1 bhaveshkulkarni4/employee-app:v1
```

## 3. Push Docker Image

```bash
docker push bhaveshkulkarni4/employee-app:v1
```

## 4. Deploy Kubernetes Resources

```bash
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/pvc.yaml
kubectl apply -f k8s/statefulset.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
kubectl apply -f k8s/hpa.yaml
```

---

# Architecture

```
                Internet
                    │
                    ▼
     Google Cloud Load Balancer
                    │
                    ▼
               Kubernetes Ingress
                    │
                    ▼
             Kubernetes Service
                    │
                    ▼
     Employee Application (2 Pods)
                    │
                    ▼
          MySQL StatefulSet
                    │
                    ▼
        Persistent Volume Claim
```

---

# Features

- Dockerized Employee Management Application
- Google Kubernetes Engine (GKE) Deployment
- Deployment with Two Replicas
- MySQL StatefulSet
- Persistent Storage using PVC
- ConfigMap for Application Configuration
- Secret for Database Credentials
- Service for Internal Communication
- Ingress for External Access
- Horizontal Pod Autoscaler (HPA)

---

# Assumptions

- Google Kubernetes Engine Standard Cluster is used.
- Docker image is hosted on Docker Hub.
- Dynamic Persistent Volume provisioning is enabled.
- MySQL stores application data.
- Application runs on port 5000.
- Service exposes port 80.
- Ingress creates a Google Cloud Load Balancer.

---

# FinOps Considerations

- Used cost-effective GKE node configuration.
- Configured Horizontal Pod Autoscaler for efficient resource utilization.
- Used Persistent Volumes to ensure data persistence.
- Docker image is reused from Docker Hub.
- Cloud resources can be deleted after assignment completion to avoid unnecessary costs.

---

# Outcome

The Employee Management Application was successfully deployed on Google Kubernetes Engine using Kubernetes best practices. The solution includes Deployment, StatefulSet, Service, Ingress, ConfigMap, Secret, Persistent Volume Claim, and Horizontal Pod Autoscaler, providing a scalable and resilient deployment.
