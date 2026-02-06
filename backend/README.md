# Backend Services

## Purpose
The backend is a service-oriented architecture that handles core platform functions: event catalog, search, booking, payments, and user profiles.

## MVP skeleton in this repo
- `app/main.py` provides a minimal FastAPI app.
- `GET /events` returns mock event data.
- `GET /recommendations` proxies to the ML service.

## Suggested services
- **Catalog Service**: event listings, venues, seating, schedules.
- **Search Service**: query, filters, and ranking signal integration.
- **Booking Service**: seat lock, hold, confirm, and rollback.
- **Payment Service**: payment orchestration and receipt issuing.
- **User Service**: authentication, preferences, loyalty.

## Data flow
1. Client requests events or bookings.
2. API gateway routes to services.
3. Services write to PostgreSQL and emit events to Kafka.
4. ML features are updated from Kafka streams.

## SLAs
- 95% of event searches < 300ms.
- 99.9% booking success rate with seat lock integrity.
