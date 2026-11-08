# ☁️ Cloud-Native Production Platform for a Microservices Application

<p align="center">
  <strong>A Containerized, Kubernetes-Orchestrated Microservices Platform with CI/CD, Monitoring and Alerting</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-FastAPI-blue?logo=python" />
  <img src="https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker" />
  <img src="https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?logo=kubernetes" />
  <img src="https://img.shields.io/badge/Prometheus-Monitoring-E6522C?logo=prometheus" />
  <img src="https://img.shields.io/badge/Grafana-Dashboard-F46800?logo=grafana" />
  <img src="https://img.shields.io/badge/GitHub-Actions-2088FF?logo=githubactions" />
</p>

---

## 📌 Project Overview

The **Cloud-Native Production Platform for a Microservices Application** is a cloud-native application platform developed to demonstrate modern DevOps and cloud engineering practices.

The project uses independently deployable microservices, Docker containerization, Kubernetes orchestration, CI/CD automation, and centralized infrastructure monitoring.

An API Gateway acts as the entry point for client requests and communicates with the Product and Order microservices.

The platform is deployed and demonstrated using a zero-cost local Kubernetes environment through Docker Desktop.

### 🎯 Project Objectives

- Design and implement a microservices-based application.
- Containerize application services using Docker.
- Deploy and manage services using Kubernetes.
- Implement automated CI/CD checks using GitHub Actions.
- Monitor infrastructure and Kubernetes resources using Prometheus and Grafana.
- Configure alert rules for application availability and resource utilization.
- Demonstrate API functionality through Swagger documentation.

---

## 🏗️ System Architecture

The platform consists of three application services:

| Service | Responsibility |
|---|---|
| API Gateway | Entry point for client requests and service communication |
| Product Service | Manages product information |
| Order Service | Handles order-related operations |

### Architecture Flow

```text
             CLIENT / USER
                   |
                   v
             API GATEWAY
                   |
          +--------+--------+
          |                 |
          v                 v
    PRODUCT SERVICE    ORDER SERVICE
          |                 |
          v                 v
    Product Data       Order Data
     (In-memory)        (In-memory)


       CONTAINERIZATION
             Docker
                |
                v
       KUBERNETES CLUSTER
                |
        Namespace: cloud-native
                |
       +--------+--------+
       |        |        |
       v        v        v
     API     PRODUCT   ORDER
   GATEWAY   SERVICE  SERVICE


       MONITORING LAYER
                |
          PROMETHEUS
                |
                v
             GRAFANA
                |
                v
       DASHBOARDS & ALERTS
```

---

## 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| API Documentation | Swagger / OpenAPI |
| Containerization | Docker |
| Local Container Environment | Docker Compose |
| Orchestration | Kubernetes |
| Kubernetes Environment | Docker Desktop / kind |
| CI/CD | GitHub Actions |
| Monitoring | Prometheus |
| Visualization | Grafana |
| Metrics Collection | node-exporter, kube-state-metrics |
| Version Control | Git and GitHub |
| Testing | Pytest |
| Public Demo Tunnel | Cloudflare Quick Tunnel |

---

## 📂 Project Structure

```text
cloud-native-production-platform/
│
├── .github/
│   └── workflows/
│       └── CI/CD workflow files
│
├── k8s/
│   ├── namespace.yaml
│   ├── api-gateway.yaml
│   ├── product-service.yaml
│   └── order-service.yaml
│
├── services/
│   ├── api-gateway/
│   ├── product-service/
│   └── order-service/
│
├── tests/
│   └── test_product_service.py
│
├── compose.yaml
├── README.md
└── Cloud_Native_Production_Platform_ppt.pptx
```

---

## 🐳 Docker Containerization

Each application service is containerized independently using Docker.

Docker Compose is used to define and run the multi-container application environment.

### Start the application

```powershell
docker compose up --build
```

### Stop the application

```powershell
docker compose down
```

---

## ☸️ Kubernetes Deployment

The application is deployed to a local Kubernetes cluster.

### Kubernetes Namespace

```text
cloud-native
```

### Deploy the application

Run these commands from the project root directory:

```powershell
kubectl apply -f k8s/namespace.yaml

kubectl apply -f k8s/product-service.yaml

kubectl apply -f k8s/order-service.yaml

kubectl apply -f k8s/api-gateway.yaml
```

### Verify Kubernetes Nodes

```powershell
kubectl get nodes
```

### Check Application Pods

```powershell
kubectl get pods -n cloud-native
```

### Check Kubernetes Services

```powershell
kubectl get services -n cloud-native
```

### Expected Application Components

- API Gateway
- Product Service
- Order Service

The services communicate internally through Kubernetes ClusterIP services.

---

## 🔄 CI/CD Pipeline

GitHub Actions is used to automate workflow checks when changes are pushed to the repository.

### CI/CD Workflow

```text
Developer
    |
    v
Git Repository
    |
    v
GitHub Push
    |
    v
GitHub Actions
    |
    v
Automated Workflow Checks
    |
    v
Validation Result
```

The workflow supports automated project validation and helps maintain code quality.

---

## 🌐 API Documentation

The application exposes REST API endpoints through the API Gateway.

### Available Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | API health check |
| GET | `/api/products` | List all products |
| GET | `/api/products/{product_id}` | Get product details |
| GET | `/api/orders` | List orders |
| POST | `/api/orders` | Disabled in public demo |

### Swagger API Documentation

Swagger UI provides an interactive interface for exploring and testing the API.

Local documentation:

```text
http://localhost:8090/docs
```

---

## 📊 Monitoring and Observability

Prometheus and Grafana are integrated to monitor application infrastructure and Kubernetes resources.

### Monitoring Components

- **Prometheus:** Collects and stores metrics.
- **Grafana:** Visualizes monitoring metrics through dashboards.
- **node-exporter:** Exposes system-level metrics.
- **kube-state-metrics:** Provides Kubernetes object and resource-state metrics.

### Custom Grafana Dashboard

Dashboard name:

**Cloud Native Production Monitoring**

The dashboard contains five monitoring panels:

| Panel | Purpose |
|---|---|
| Prometheus Target Health | Monitors target availability |
| CPU Usage (%) | Displays CPU utilization |
| Memory Usage (%) | Displays memory utilization |
| Disk Usage (%) | Displays filesystem utilization |
| Kubernetes Pod Status | Displays application pod states |

### Grafana Access

Local Grafana URL:

```text
http://localhost:3000
```

Grafana login credentials are configured locally.

---

## 🚨 Alerting and Notification Rules

Four Grafana-managed alert rules have been configured.

| Alert Rule | Condition | Threshold |
|---|---|---|
| API-Gateway-Down | API Gateway pod readiness | Below 1 |
| High-CPU-Usage | CPU utilization | Above 80% |
| High-Memory-Usage | Memory utilization | Above 85% |
| High-Disk-Usage | Filesystem utilization | Above 85% |

### Evaluation Configuration

- Evaluation Group: `cloud-native-alerts`
- Evaluation Interval: 1 minute
- Pending Period: 1 minute

**Verification:** All four rules were observed in Normal state during the project verification.

**Notification status:** The email contact point is configured, but SMTP is not configured. Actual email delivery has not been verified.

---

## 🧪 Testing and Validation

The project was validated through API testing, Kubernetes health checks, and automated Python tests.

### API Verification Results

| Test | Result |
|---|---|
| API Gateway health check | HTTP 200 |
| Product listing | Successful |
| Order listing | Successful |
| Public write-operation protection | HTTP 403 |
| Python automated tests | 2 passed |
| Kubernetes application pods | Running |

### Pytest Execution

```powershell
pytest -v
```

### Verified Test Results

```text
tests/test_product_service.py::test_health PASSED
tests/test_product_service.py::test_products PASSED

2 passed
```

---

## 🔐 Public Demo and Security

The public demonstration uses a Cloudflare Quick Tunnel connected to the local API Gateway.

### Public API

https://bestsellers-odds-waiver-allocation.trycloudflare.com

### Swagger Documentation

https://bestsellers-odds-waiver-allocation.trycloudflare.com/docs

### Public Demo Security

The public demonstration is configured in read-only mode.

- GET requests are available for demonstration.
- Write operations are disabled.
- POST requests return HTTP 403 Forbidden.

**Important:** The public URL is temporary. It works only while the local Kubernetes environment, application services, and Cloudflare tunnel process are running. It is not a permanent production deployment.

---

## 📥 Project Presentation

The complete project presentation is available in this repository.

**[Download Cloud-Native Production Platform – PowerPoint Presentation](./Cloud_Native_Production_Platform_ppt.pptx)**

---

## ⚠️ Current Limitations

- The application runs on local Docker Desktop Kubernetes rather than AWS EKS.
- No paid AWS infrastructure has been provisioned.
- Order data is stored in memory and is not persistent across application restarts.
- SMTP email notification delivery has not been verified.
- The Cloudflare Quick Tunnel URL is temporary.

---

## 🚀 Future Enhancements

- Integrate a persistent database for order management.
- Implement authentication and authorization.
- Add AI-powered intelligent log analysis and incident classification.
- Improve secrets management and application security.
- Implement Kubernetes autoscaling and resource optimization.
- Configure and verify email or webhook notifications.
- Deploy to a managed cloud Kubernetes environment when budget permits.

---

## 👨‍💻 Author

**Neeraj Lodhi**

Final-Year B.Tech Computer Science Engineering  
Specialization: Cyber Security

### GitHub Repository

https://github.com/Neerajlo/cloud-native-production-platform

---

## ⭐ Acknowledgement

This project demonstrates practical implementation of cloud-native architecture, microservices, containerization, Kubernetes orchestration, CI/CD automation, and infrastructure observability using a zero-cost local development environment.

**Thank you for visiting this project!**
