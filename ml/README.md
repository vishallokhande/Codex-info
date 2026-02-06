# ML Platform

## Purpose
Provide personalized recommendations, demand forecasting, and fraud detection signals for the booking platform.

## MVP skeleton in this repo
- `app/main.py` returns static ranked events to simulate a model response.
- `GET /rank` is called by the backend `/recommendations` route.

## Core models
- **Recommendation model**: rank events per user.
- **Demand forecasting**: predict ticket sales per event.
- **Anomaly detection**: detect suspicious traffic spikes.

## Pipeline stages
1. Ingest events and user behavior streams.
2. Feature extraction and validation.
3. Training with model registry and experiment tracking.
4. Batch scoring and real-time inference services.

## Serving patterns
- **Real-time**: FastAPI inference service for ranking.
- **Batch**: Nightly demand forecasting jobs.
