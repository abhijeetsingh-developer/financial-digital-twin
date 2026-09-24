# Implementation Stages

## Stage 1 — Financial Input
Collect income, expenses, savings, purchase and EMI values.

## Stage 2 — Cash Runway
Calculate:

runway = savings / monthly expenses

## Stage 3 — Digital Twin
Represent the user's current financial state as a reusable object/state.

## Stage 4 — What-If Scenario
Create a simulated copy of the financial state and change one or more variables.

Examples:
- Cash purchase
- EMI purchase
- Delayed purchase
- Income drop
- Expense rise

## Stage 5 — Stress Score
Use a transparent deterministic prototype score from 0–100.

Important: the current formula is a hackathon prototype and is not a validated financial-risk score.

## Stage 6 — Backend
Expose the deterministic engine through FastAPI.

Endpoint:
POST /simulate

## Stage 7 — Frontend
Build the dashboard with:
- financial inputs
- scenario selector
- stress score
- cash runway
- monthly buffer

## Stage 8 — AI
Only after the mathematical engine works:
- explain results in plain language
- suggest relevant scenarios
- parse natural-language questions

AI should not perform the core financial calculations.

## Stage 9 — Later Expansion
Possible later additions from the proposal:
- Open Banking / Account Aggregator integration
- transaction categorization
- multi-goal optimization
- database
- authentication
- deployment
- fintech API / SDK
