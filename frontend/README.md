# Frontend App

## Purpose
The frontend provides a fast, personalized event discovery and booking experience.

## MVP skeleton in this repo
- `index.html` renders a simple UI for events, recommendations, and health.
- It proxies API calls to the backend and ML service through Nginx.

## Pages
- Home with recommended events.
- Search and filter by location, price, genre, and date.
- Event details with seating, rating, and availability.
- Checkout with secure payment flow.

## Performance goals
- First contentful paint under 2.5s on average connections.
- Real-time seat availability with optimistic updates.
