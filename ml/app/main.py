from fastapi import FastAPI


app = FastAPI(title="SeatSense Live ML Service")


@app.get("/health")
def health():
    return {"status": "ok", "service": "ml"}


@app.get("/rank")
def rank_events(user_id: str = "guest"):
    return {
        "user_id": user_id,
        "ranked_events": [
            {"id": "evt_103", "score": 0.93},
            {"id": "evt_101", "score": 0.87},
            {"id": "evt_102", "score": 0.81},
        ],
        "model_version": "v0.1.0",
    }
