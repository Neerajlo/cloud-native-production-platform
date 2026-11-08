\# Cloud-Native Production Platform for a Microservices Application



\## Project Overview



This project demonstrates a cloud-native microservices application built using Python, FastAPI, Docker, and Docker Compose.



The application uses an API Gateway to communicate with independent Product and Order services.



\## Architecture



The platform consists of three microservices:



1\. \*\*API Gateway\*\* – Entry point for client requests.

2\. \*\*Product Service\*\* – Manages product information.

3\. \*\*Order Service\*\* – Handles order-related operations.



\## Technology Stack



\- Python

\- FastAPI

\- Docker

\- Docker Compose

\- REST APIs

\- Pytest

\- GitHub Actions



\## Project Structure



```text

cloud-native-production-platform/

├── .github/workflows/

│   └── ci.yml

├── services/

│   ├── api-gateway/

│   ├── product-service/

│   └── order-service/

├── tests/

│   └── test\_product\_service.py

├── compose.yaml

└── README.md

```



\## Prerequisites



\- Python 3.12+

\- Docker Desktop

\- Git



## Run the Application



Clone the repository:



```bash

git clone https://github.com/Neerajlo/cloud-native-production-platform.git

cd cloud-native-production-platform

```



Start the services:



```bash

docker compose up --build

```
## Deploy to Kubernetes

Create the Kubernetes namespace:

```bash
kubectl apply -f k8s/namespace.yaml

kubectl apply -f k8s/product-service.yaml
kubectl apply -f k8s/order-service.yaml
kubectl apply -f k8s/api-gateway.yaml
```
Check deployment status:

```bash
kubectl get pods -n cloud-native
kubectl get services -n cloud-native
kubectl get deployments -n cloud-native
```

Access API Gateway:

```bash
kubectl port-forward -n cloud-native svc/api-gateway 8081:8080
```

Swagger documentation: http://localhost:8081/docs

Stop the services:



```bash

docker compose down

```



\## API Documentation



Once the application is running:



| Service | URL |

|---|---|

| API Gateway | http://localhost:8080/docs |

| Product Service | http://localhost:8001/docs |

| Order Service | http://localhost:8002/docs |



\## Testing



Run automated tests:



```bash

python -m pytest -q tests/test\_product\_service.py

```



\## Continuous Integration



GitHub Actions is configured to run automated tests and build Docker images when changes are pushed or a pull request is created.



\## Future Enhancements




\- Helm charts

\- Argo CD GitOps

\- Prometheus and Grafana monitoring

\- Centralized logging

\- Security and reliability improvements



## Monitoring with Prometheus and Grafana

The project uses Prometheus and Grafana for monitoring Kubernetes workloads and infrastructure.

### Monitoring Components

- Prometheus for metrics collection and querying.
- Grafana for dashboard visualization.
- Node Exporter for system-level metrics.
- Kubernetes monitoring through kube-prometheus-stack.

### Grafana Dashboard

Dashboard Name: Cloud Native Production Monitoring

The dashboard includes:

- Prometheus Target Health
- CPU Usage (%)
- Memory Usage (%)
- Disk Usage (%)
- Kubernetes Pod Status

### Access Grafana

Start port forwarding:

```bash
kubectl port-forward deployment/monitoring-grafana 3000:3000 -n monitoring
```

Open Grafana in your browser:

http://localhost:3000

### Verify Monitoring Pods

```bash
kubectl get pods -n monitoring
```
## Public Demo (Temporary)

The API Gateway is accessible through a temporary Cloudflare Quick Tunnel.

**Public API URL:**
https://bestsellers-odds-waiver-allocation.trycloudflare.com

**Swagger API Documentation:**
https://bestsellers-odds-waiver-allocation.trycloudflare.com/docs

### Available Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | API health check |
| GET | `/api/products` | List all products |
| GET | `/api/products/{product_id}` | Get product details |
| GET | `/api/orders` | List orders |
| POST | `/api/orders` | Disabled in public demo |

**Security:** Public demo is configured as read-only. Write operations return HTTP 403 Forbidden.

**Note:** This is a temporary Cloudflare Quick Tunnel. The URL is available only while the tunnel and local Kubernetes environment are running. It is not a permanent production deployment.

---

## Project Presentation

[📥 Download Project PPT](./Cloud_Native_Production_Platform_ppt.pptx)

## Author

Neeraj Lodhi


