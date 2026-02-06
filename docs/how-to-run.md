# How to Run SeatSense Live (Implementation Guide)

## Current status
This repository includes a **runnable MVP skeleton** (frontend + backend + ML service) and a blueprint for the full production system. Use the instructions below to run the stack locally.

---

## Option A: Start with a local dev stack (recommended for MVP)

### 1) Run locally
From the repo root:
```
docker compose up --build
```

### 2) Validate
- Frontend: http://localhost:8080
- Backend health: http://localhost:8000/health
- ML health: http://localhost:9000/health

---

## Option B: Run without Docker (local or VM)

### 1) Start the ML service
```
python -m venv .venv
source .venv/bin/activate
pip install -r ml/requirements.txt
uvicorn ml.app.main:app --reload --port 9000
```

### 2) Start the backend service (new terminal)
```
source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload --port 8000
```

### 3) Start the frontend (new terminal)
```
cd frontend
python -m http.server 8080
```

### 4) Validate
- Frontend: http://localhost:8080
- Backend health: http://localhost:8000/health
- ML health: http://localhost:9000/health

---

## Option C: Start with a Kubernetes dev cluster

### 1) Provision cluster
Use Terraform modules in `infra/` to stand up a dev cluster.

### 2) Deploy with GitOps
Use Argo CD or Flux to sync workloads from your Git repo.

### 3) Deploy in order
1. Datastores (Postgres, Redis, Kafka)
2. Backend services
3. ML services
4. Frontend

---

## What to add next (if you want this repo to grow)
1. Expand backend domain models and data persistence.
2. Replace the static frontend with a full Next.js app.
3. Add Kafka/Redis/Postgres services to the compose stack.
4. Add CI/CD pipelines in `ci/`.

If you want, I can implement this runnable skeleton for you in the next iteration (API + UI + compose + basic CI).
