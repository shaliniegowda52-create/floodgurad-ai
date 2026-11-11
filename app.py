from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "project": "FloodGuard AI"})

@app.post("/api/risk")
def estimate_risk():
    payload = request.get_json(silent=True) or {}
    required = ["rainfall_mm", "elevation_m"]
    missing = [key for key in required if key not in payload]
    if missing:
        return jsonify({"error": "Missing required fields", "fields": missing}), 400

    # Transparent demo baseline only. Replace with a trained and evaluated model.
    rainfall = float(payload["rainfall_mm"])
    elevation = float(payload["elevation_m"])
    score = min(1.0, max(0.0, 0.7 * min(rainfall / 150.0, 1.0)
                         + 0.3 * (1.0 - min(max(elevation, 0.0) / 100.0, 1.0))))
    if score >= 0.65:
        level = "high"
    elif score >= 0.35:
        level = "moderate"
    else:
        level = "low"

    return jsonify({
        "risk_level": level,
        "demo_score": round(score, 3),
        "status": "simulated_demo",
        "message": "Illustrative baseline only; not an operational flood forecast."
    })

if __name__ == "__main__":
    app.run(debug=True)
