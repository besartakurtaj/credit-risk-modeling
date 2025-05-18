# Credit Risk Modeling Project

This repository contains a complete workflow for credit risk modeling, including data generation, cleaning, feature engineering, modeling, and an interactive dashboard for visualization.

---

## Project Overview

The goal of this project is to build a credit risk model to estimate Expected Credit Loss (ECL) using synthetic loan data and macroeconomic indicators. The workflow covers:

* **Data generation:** Simulate loan and macroeconomic datasets
* **Data cleaning:** Prepare and clean the data for analysis
* **Feature engineering:** Create relevant features for modeling
* **Modeling:** Develop models for Probability of Default (PD), Loss Given Default (LGD), and Exposure at Default (EAD)
* **Dashboard:** Interactive visualization of model outputs using Streamlit

---

## Getting Started

### Prerequisites
* Install required packages:

```bash
pip install -r requirements.txt
```

---

### Data Generation

The synthetic datasets are generated using the `generate_data.py` script:

* **Synthetic loan data:** Simulates loan attributes such as Credit Score, Income, Loan Amount, Customer Age, and Default status.
* **Macroeconomic indicators:** Simulates time series data for GDP Growth, Unemployment Rate, and Inflation.

Run this script first to create the input CSV files:

```bash
python generate_data.py
```

This will create the following files in the `data/` folder:

* `synthetic_loan_data.csv`
* `macroeconomic_indicators.csv`

---

### Data Cleaning and Feature Engineering

The data cleaning script (`01_data_cleaning.py`) prepares the raw data, converting data types and handling missing values.

The feature engineering script (`02_feature_engineering.py`) creates new features such as Debt-to-Income ratio, Age groups, and rolling macroeconomic averages.

---

### Modeling

Scripts like `03_modeling_PD_LGD_EAD.py` build models for the components of Expected Credit Loss:

* Probability of Default (PD)
* Loss Given Default (LGD)
* Exposure at Default (EAD)

---

### ECL Calculation

The script `04_ECL_calculation` calculates Expected Credit Loss (ECL) based on the modeling outputs

---

### Dashboard

An interactive dashboard is provided in `app/dashboard.py`, built with Streamlit. It allows visualization of:

* Portfolio metrics and KPIs
* ECL by credit score bands
* Scatter plots of PD vs EAD with bubble size representing ECL

To run the dashboard locally:

```bash
streamlit run app/dashboard.py
```

![image](https://github.com/user-attachments/assets/fda02216-2516-44b8-a34b-7a9c642ae7c0)
![image](https://github.com/user-attachments/assets/25fd132f-b97f-4e3c-942f-e5c056d4867f)



Make sure to generate and process the data first, so the dashboard can load `final_dashboard_data.csv` from the `data/` folder.



