# Frontend App

## Purpose
The frontend provides a fast, personalized event discovery and booking experience.

## MVP skeleton in this repo
- `index.html` renders a simple UI for events, recommendations, and health.
- It calls the backend and ML service directly in dev mode. You can override the base
  URLs by setting `window.API_BASE` and `window.ML_BASE` in the browser console.

## Pages
- Home with recommended events.
- Search and filter by location, price, genre, and date.
- Event details with seating, rating, and availability.
- Checkout with secure payment flow.

## Performance goals
- First contentful paint under 2.5s on average connections.
- Real-time seat availability with optimistic updates.
