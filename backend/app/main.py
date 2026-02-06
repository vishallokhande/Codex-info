import os

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="SeatSense Live Backend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

ML_SERVICE_URL = os.getenv("ML_SERVICE_URL", "http://localhost:9000")


@app.get("/health")
def health():
    return {"status": "ok", "service": "backend"}


@app.get("/events")
def list_events():
    return {
        "events": [
            {
                "id": "evt_101",
                "title": "City Jazz Night",
                "venue": "Riverside Hall",
                "date": "2025-04-12",
            },
            {
                "id": "evt_102",
                "title": "Indie Film Premiere",
                "venue": "Aurora Theater",
                "date": "2025-04-18",
            },
            {
                "id": "evt_103",
                "title": "Championship Finals",
                "venue": "Metro Arena",
                "date": "2025-05-02",
            },
        ]
    }


@app.get("/recommendations")
async def recommendations(user_id: str = "guest"):
    async with httpx.AsyncClient(timeout=3.0) as client:
        response = await client.get(f"{ML_SERVICE_URL}/rank", params={"user_id": user_id})
        response.raise_for_status()
    return response.json()
