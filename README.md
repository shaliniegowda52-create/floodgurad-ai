# FloodGuard AI

**AI-powered, location-aware flood-risk insights and emergency decision support.**

FloodGuard AI is a hackathon prototype that combines available rainfall, terrain, land-cover and historical flood information to estimate an area-level risk category and explain the factors behind it.

> **Safety note:** This is a decision-support prototype, not an official flood-warning service. Do not use it as the sole basis for evacuation or emergency decisions. Follow local authorities and emergency services.

## Team
- Shalini
- Ritheeksha
- Shree Madhura
- Sushmitha

## MVP scope
1. Select a demonstration location.
2. View clearly labelled environmental inputs.
3. Estimate Low / Moderate / High risk using a baseline model.
4. Explain the strongest contributing input factors.
5. Show preparedness guidance and verified emergency resources.

## Architecture
- Frontend: React
- Backend: Python + Flask
- ML: scikit-learn
- Map: OpenStreetMap
- Prototype data: CSV / SQLite

## Repository structure
```text
floodguard-ai/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── data/
│       └── README.md
├── ml/
│   ├── train.py
│   └── README.md
├── frontend/
│   └── README.md
├── docs/
│   └── idea-submission.md
└── README.md
```

## Run the backend
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
The API runs at `http://127.0.0.1:5000`.

## Data and evaluation
Use a documented, geographically relevant dataset. Keep source, licence, date range, geographic coverage and missing-value handling in the repository. Split data by time or geography where appropriate to reduce leakage. Report precision, recall, F1-score and a confusion matrix on held-out data. Never invent model accuracy.

## Data labels in the UI
Every input must be labelled as one of:
- Observed/live
- Forecast
- Historical
- Simulated/demo

Never present simulated data as live observations.
