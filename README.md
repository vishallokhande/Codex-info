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
├── ci/
└── docs/
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

## Next steps
See each module README for deeper setup notes:
- [backend/README.md](backend/README.md)
- [frontend/README.md](frontend/README.md)
- [ml/README.md](ml/README.md)
- [infra/README.md](infra/README.md)
- [ci/README.md](ci/README.md)
- [docs/README.md](docs/README.md)

Additional guidance:
- [docs/project-brief.md](docs/project-brief.md)
- [docs/how-to-run.md](docs/how-to-run.md)
