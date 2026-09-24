from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal

app = FastAPI(title="Financial Digital Twin API")


class FinancialInput(BaseModel):
    income: float = Field(gt=0)
    expenses: float = Field(ge=0)
    savings: float = Field(ge=0)
    purchase: float = Field(default=0, ge=0)
    emi: float = Field(default=0, ge=0)
    scenario: Literal["baseline", "cash", "emi", "delay", "income_drop", "expense_rise"] = "baseline"


def calculate_runway(savings: float, monthly_expenses: float) -> float:
    if monthly_expenses <= 0:
        return 999.0
    return round(savings / monthly_expenses, 1)


def calculate_stress(income: float, expenses: float, savings: float) -> int:
    # Simple transparent hackathon MVP score.
    # This is a prototype metric, not a validated financial-risk model.
    monthly_buffer = income - expenses
    expense_ratio = expenses / income if income else 1

    score = 0

    if expense_ratio >= 0.8:
        score += 35
    elif expense_ratio >= 0.65:
        score += 25
    elif expense_ratio >= 0.5:
        score += 15

    if monthly_buffer <= 0:
        score += 35
    elif monthly_buffer < income * 0.15:
        score += 20

    runway = calculate_runway(savings, expenses)
    if runway < 3:
        score += 30
    elif runway < 6:
        score += 20
    elif runway < 12:
        score += 10

    return max(0, min(100, score))


def simulate(data: FinancialInput):
    income = data.income
    expenses = data.expenses
    savings = data.savings

    if data.scenario == "cash":
        savings -= data.purchase

    elif data.scenario == "emi":
        expenses += data.emi

    elif data.scenario == "delay":
        # MVP assumption: no purchase today; savings continue for 3 months.
        savings += max(0, income - expenses) * 3

    elif data.scenario == "income_drop":
        income *= 0.85

    elif data.scenario == "expense_rise":
        expenses *= 1.10

    monthly_buffer = income - expenses
    runway = calculate_runway(savings, expenses)
    stress = calculate_stress(income, expenses, savings)

    return {
        "scenario": data.scenario,
        "income": round(income, 2),
        "expenses": round(expenses, 2),
        "savings": round(savings, 2),
        "monthly_buffer": round(monthly_buffer, 2),
        "runway_months": runway,
        "stress_score": stress,
        "risk_level": (
            "Low" if stress < 30 else
            "Moderate" if stress < 60 else
            "High"
        )
    }


@app.get("/")
def root():
    return {"message": "Financial Digital Twin API is running"}


@app.post("/simulate")
def run_simulation(data: FinancialInput):
    return simulate(data)
