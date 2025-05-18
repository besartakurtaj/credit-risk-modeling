"""
generate_data.py

This script generates synthetic loan and macroeconomic datasets for use in credit risk modeling.
It creates a realistic portfolio of loan records with borrower features and default outcomes,
as well as macroeconomic indicators over time.

Outputs:
- synthetic_loan_data.csv: Contains simulated loan-level data including CreditScore, Income, LoanAmount, etc.
- macroeconomic_indicators.csv: Contains time-series data for GDP growth, unemployment, and inflation.

These datasets are used for feature engineering, modeling (PD, LGD, EAD), and dashboard visualization.
"""

import pandas as pd
import numpy as np
from faker import Faker
from datetime import timedelta, datetime
import random
import os

fake = Faker()
np.random.seed(42)
random.seed(42)

os.makedirs("data", exist_ok=True)

def generate_loan_record(i):
    origination_date = fake.date_between(start_date='-3y', end_date='-1y')
    term_months = random.choice([12, 24, 36, 48, 60])
    end_date = origination_date + timedelta(days=30 * term_months)

    defaulted = np.random.binomial(1, 0.2)
    default_date = fake.date_between(start_date=origination_date, end_date=end_date) if defaulted else None

    return {
        "LoanID": f"L{i:05d}",
        "CustomerAge": np.random.randint(21, 70),
        "Income": np.random.randint(20000, 150000),
        "LoanAmount": np.random.randint(3000, 50000),
        "InterestRate": round(np.random.uniform(4.0, 18.0), 2),
        "TermMonths": term_months,
        "CreditScore": np.random.randint(300, 850),
        "OriginationDate": origination_date,
        "Defaulted": defaulted,
        "DefaultDate": default_date,
    }

loan_data = pd.DataFrame([generate_loan_record(i) for i in range(5000)])
loan_data.to_csv("data/synthetic_loan_data.csv", index=False)

# Monthly from 3 years ago to today
dates = pd.date_range(start="2020-01-01", end=datetime.today(), freq='M')
macro_data = pd.DataFrame({
    "Date": dates,
    "GDP_Growth": np.random.normal(2.0, 0.5, len(dates)),         # in %
    "Unemployment_Rate": np.random.normal(6.0, 1.0, len(dates)),  # in %
    "Inflation_Rate": np.random.normal(2.5, 0.3, len(dates)),     # in %
})
macro_data["Date"] = macro_data["Date"].dt.date
macro_data.to_csv("data/macroeconomic_indicators.csv", index=False)

print("Data generated in /data folder")
