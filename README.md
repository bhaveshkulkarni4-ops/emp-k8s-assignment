# emp-k8s-assignment
# Employee Management Application Deployment on Google Kubernetes Engine

## 1. Project Overview

This project demonstrates the deployment of a containerized Employee Management application on Google Kubernetes Engine (GKE) using Kubernetes best practices. The application is packaged as a Docker container, pushed to Docker Hub, and deployed on a GKE Standard Cluster. The solution includes persistent storage for the MySQL database, secure configuration management, external application access through Ingress, and automatic scaling using Horizontal Pod Autoscaler (HPA).

---

# 2. Technology Stack

* Python Flask
* MySQL 8.0
* Docker
* Docker Hub
* Google Kubernetes Engine (GKE)
* Kubernetes
* GitHub

---

# 3. Kubernetes Components Used

| Component                     | Purpose                                                        |
| ----------------------------- | -------------------------------------------------------------- |
| Deployment                    | Deploys and manages Employee application pods                  |
| StatefulSet                   | Deploys MySQL database with stable storage                     |
| Service                       | Exposes the application internally within the cluster          |
| Ingress                       | Provides external access through Google Cloud Load Balancer    |
| ConfigMap                     | Stores application configuration                               |
| Secret                        | Stores database credentials securely                           |
| Persistent Volume Claim (PVC) | Provides persistent storage for MySQL                          |
| Horizontal Pod Autoscaler     | Automatically scales application pods based on CPU utilization |

---

# 4. Deployment Steps

## Step 1

Build Docker Image

docker build -t employee-app:v1 .

## Step 2

Push Docker Image

docker tag employee-app:v1 bhaveshkulkarni4/employee-app:v1

docker push bhaveshkulkarni4/employee-app:v1

## Step 3

Create Kubernetes Resources

kubectl apply -f k8s/configmap.yaml

kubectl apply -f k8s/secret.yaml

kubectl apply -f k8s/pvc.yaml

kubectl apply -f k8s/statefulset.yaml

kubectl apply -f k8s/deployment.yaml

kubectl apply -f k8s/service.yaml

kubectl apply -f k8s/ingress.yaml

kubectl apply -f k8s/hpa.yaml

---

# 5. Architecture

Internet

↓

Google Cloud Load Balancer

↓

Kubernetes Ingress

↓

Kubernetes Service

↓

Employee Application Deployment (2 Replicas)

↓

MySQL StatefulSet

↓

Persistent Volume

---

# 6. Features Implemented

* Dockerized Employee application
* Docker image published to Docker Hub
* Kubernetes Deployment with two replicas
* MySQL StatefulSet
* Persistent Volume Claim for database persistence
* ConfigMap for configuration management
* Secret for secure credential storage
* Kubernetes Service for internal communication
* Kubernetes Ingress for external access
* Horizontal Pod Autoscaler (HPA)
* Google Kubernetes Engine deployment

---

# 7. Assumptions

* Docker image is available on Docker Hub.
* Google Kubernetes Engine Standard Cluster is used.
* Dynamic Persistent Volume provisioning is enabled.
* MySQL is used as the backend database.
* Application listens on port 5000.
* Service exposes the application on port 80.
* Google Cloud Load Balancer is automatically created through Kubernetes Ingress.

---

# 8. FinOps Considerations

* Used e2-medium worker nodes to balance cost and performance.
* Configured Horizontal Pod Autoscaler to scale only when required.
* Used Persistent Volume instead of local storage to avoid data loss.
* Docker image is reused from Docker Hub to reduce deployment time.
* GKE resources will be deleted after assignment completion to prevent unnecessary cloud costs.

---

# 9. Challenges Faced

* MySQL pod remained in ContainerCreating state due to the original node becoming unavailable.
* Persistent Volume attachment prevented the pod from starting on another node.
* Created a new node pool and removed the unavailable node.
* Updated the Ingress configuration by removing host-based routing to allow access through the external IP.
* Successfully validated application deployment after resolving infrastructure issues.

---

# 10. Outcome

The Employee Management application was successfully deployed on Google Kubernetes Engine. All Kubernetes resources including Deployment, StatefulSet, Service, Ingress, ConfigMap, Secret, Persistent Volume Claim, and Horizontal Pod Autoscaler were created successfully. The application is accessible through the Kubernetes Ingress and Google Cloud Load Balancer.
