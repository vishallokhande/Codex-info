# SeatSense Live

SeatSense Live is a real-time event discovery and booking platform inspired by the pace and scale of entertainment ticketing, without copying any existing product. It combines a modern web experience with AI/ML-driven personalization and a DevOps-first automation backbone to deliver fast, reliable, and highly relevant event experiences.

**What this repo is right now:** a **runnable MVP skeleton** plus a project blueprint. You can start the local stack with Docker Compose to see a working frontend, backend API, and ML ranking service. The code is intentionally minimal so teams can extend it into a full production implementation.

## Why this project exists
- **Audience problem**: People want to find the right events quickly, at the right price, in the right place, without endless searching.
- **Organizer problem**: Event organizers need to forecast demand, reduce no-show risk, and set dynamic pricing without guesswork.
- **Platform problem**: The system must handle traffic spikes, prevent overselling, and maintain very low latency.

## Where it is used
SeatSense Live targets:
- City-wide cultural events, theaters, sports, and community venues.
- Corporate event platforms for internal reservations.
- Campus or enterprise booking systems.

## Core product goals
- **Fast discovery** of relevant events for each user.
- **Safe, consistent transactions** even under heavy traffic.
- **Smart recommendations** and pricing decisions powered by AI/ML.
- **Operational automation** from code to production with minimal manual intervention.

---

## Project structure
```
.
├── backend/
├── frontend/
├── ml/
├── infra/
└── ci/
```

---

## Architecture overview (high level)
```
Users -> Web App -> API Gateway -> Services (Search, Booking, Payments, Catalog)
                                  -> Event Data Store (Postgres)
                                  -> Cache (Redis)
                                  -> Message Bus (Kafka)
                                  -> ML Services (Rec Engine, Demand Forecast)
                                  -> Observability (Prometheus + Grafana + OTel)
```

---

## AI/ML in this platform (what + why + how)
### 1. Personalized Recommendations
- **What**: Rank events per user based on location, preferences, past purchases, and time.
- **Why**: Increases discovery speed and conversion rate.
- **How**: User embeddings + event embeddings + ranking model (e.g., LightGBM or deep ranking).

### 2. Demand Forecasting
- **What**: Predict booking demand per event over time.
- **Why**: Helps organizers and platform adjust pricing, inventory, and marketing spend.
- **How**: Time-series forecasting (Prophet, XGBoost, or LSTM).

### 3. Dynamic Pricing Signals
- **What**: Recommend pricing adjustments based on demand, seat availability, and seasonality.
- **Why**: Improves revenue while avoiding sudden price shocks.
- **How**: Regression/optimization model with guardrails.

### 4. Fraud/Abuse Detection
- **What**: Detect suspicious booking bursts and bot activity.
- **Why**: Protects inventory and user trust.
- **How**: Anomaly detection on traffic and booking patterns.

---

## DevOps automation plan (what + why + how)
### 1. CI/CD
- **Build**: Lint, test, and containerize all services.
- **Release**: Promote container images with signed provenance.
- **Deploy**: GitOps-style deployments with environment promotion.

### 2. Infrastructure as Code
- **Why**: Consistent, auditable, repeatable infrastructure.
- **How**: Terraform modules for networking, Kubernetes, and data services.

### 3. Observability and SLOs
- **Why**: Ensure low latency and prevent booking failures.
- **How**: OpenTelemetry for traces, Prometheus for metrics, Grafana for dashboards, alerting via PagerDuty/Slack.

### 4. Security Automation
- **Why**: Reduce risk in a payment and identity-heavy system.
- **How**: SAST/DAST, container scanning, secret detection, and IAM least privilege.

---

## How this platform is faster because of AI/ML
- **Reduced search time** with personalized ranking.
- **Lower cart abandonment** by predicting high-demand events and recommending earlier.
- **Better inventory turnover** with forecast-driven promotions.
- **Operational efficiency** by automated anomaly detection and incident response.

---

## Tech stack (suggested)
**Frontend**
- Next.js + TypeScript + Tailwind

**Backend**
- Node.js (NestJS) or Go (Gin)
- PostgreSQL + Redis
- Kafka for event streaming

**ML**
- Python + FastAPI
- MLflow for experiment tracking
- Feast for feature store

**Infra**
- Kubernetes (EKS/GKE/AKS)
- Terraform
- Argo CD for GitOps

**Observability**
- OpenTelemetry + Prometheus + Grafana + Loki

---

## Module responsibilities (current MVP)
- **backend/**: FastAPI service that serves event listings and proxies recommendation requests to the ML service.
- **ml/**: FastAPI service that returns ranked event IDs with mock scores.
- **frontend/**: Static UI that calls the backend/ML APIs directly in dev mode.
- **infra/**: Placeholder for Terraform/Kubernetes manifests as the project scales.
- **ci/**: Placeholder for CI/CD workflows and release automation.

---

## How to run (local)

### Option A: Docker Compose (recommended)
From the repo root:
```
docker compose up --build
```

Validate:
- Frontend: http://localhost:8080
- Backend health: http://localhost:8000/health
- ML health: http://localhost:9000/health

### Option B: Run without Docker (local or VM)

1) Start the ML service:
```
python -m venv .venv
source .venv/bin/activate
pip install -r ml/requirements.txt
uvicorn ml.app.main:app --reload --port 9000
```

2) Start the backend service (new terminal):
```
source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload --port 8000
```

3) Start the frontend (new terminal):
```
cd frontend
python -m http.server 8080
```

Validate:
- Frontend: http://localhost:8080
- Backend health: http://localhost:8000/health
- ML health: http://localhost:9000/health

---

## How to push this project to your GitHub repository
1) Initialize git (if needed):
```
git init
```

2) Add the files:
```
git add .
```

3) Commit:
```
git commit -m "Initial SeatSense Live MVP"
```

4) Create a GitHub repo and add the remote:
```
git remote add origin https://github.com/<your-username>/<your-repo>.git
```

5) Push:
```
git branch -M main
git push -u origin main
```
