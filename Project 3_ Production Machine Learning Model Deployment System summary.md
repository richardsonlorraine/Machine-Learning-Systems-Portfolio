Summary 
Project 3: Production Machine Learning Model Deployment System

* Core Focus: Developing a production-grade, containerized MLOps infrastructure to serve real-time REST APIs scalably and resiliently.

* Technologies Used: Flask, joblib, Docker, Azure Container Registry (ACR), and Azure Kubernetes Service (AKS).

* System Architecture:

	Trained Model -> Flask Inference API -> Docker Containerization -> AKS Cloud Orchestration/Load Balancing -> Client Request Prediction.

Key Mechanisms & Results:

* Inference API: A stateless Flask API that loads serialized models into memory for low-latency JSON request handling.

* Containerization: Built immutable, optimized environments utilizing python: 3.9-slim with absolute dependency pinning.

* Orchestration & CI/CD: Automated cloud deployments to AKS via a CI/CD pipeline (triggered on code commit). Achieved auto-scaling, high availability, an automated deployment time of <15 minutes, and a P99 latency of <150.
