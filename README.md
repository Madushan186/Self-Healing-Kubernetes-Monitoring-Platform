# Self-Healing Kubernetes Monitoring Platform

## Overview
This project demonstrates a production-style DevOps setup using Docker, Kubernetes, Prometheus, and Grafana.

A FastAPI application is containerized and deployed on Kubernetes with multiple replicas. The system is designed to be self-healing, automatically recovering from failures, while providing real-time monitoring and visualization.

## Tech Stack
- FastAPI
- Docker
- Kubernetes (Minikube)
- Prometheus
- Grafana

## Features
- Containerized application using Docker
- Kubernetes Deployment with 2 replicas
- Liveness and Readiness Probes
- Self-healing through automatic pod recreation
- Prometheus metrics scraping with ServiceMonitor
- Grafana dashboard visualization

## Monitoring Dashboard
The dashboard includes:
- Total Requests
- Requests Per Second
- Average Response Time
- Requests by Endpoint

## Project Structure
```text
self-healing-platform/
├── app/
├── k8s/
├── dashboards/
│   └── self-healing-dashboard.json
├── Dockerfile
├── requirements.txt
└── README.md

## 📸 Screenshots

### Dashboard
![Dashboard](docs/dashboard.png)

### Running Pods
![Pods](docs/pods.png)

### Self-Healing
![Self-Healing](docs/self-healing.png)
