# Financial Digital Twin — Hackathon MVP

This starter project follows the staged implementation described in the Financial Digital Twin slide deck:

1. Financial input
2. Cash runway
3. Digital Twin state
4. What-if scenarios
5. Stress score
6. FastAPI backend
7. Frontend
8. AI explanation

The MVP currently implements the deterministic financial engine and FastAPI API, plus a simple browser frontend.

## Run backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000

## API

POST `/simulate`

Example JSON:

```json
{
  "income": 40000,
  "expenses": 25000,
  "savings": 80000,
  "purchase": 60000,
  "emi": 5500,
  "scenario": "emi"
}
```

The calculation engine is deterministic. AI is intentionally not used for financial calculations.
