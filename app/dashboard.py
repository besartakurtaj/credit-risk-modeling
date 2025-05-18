import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

"""
Streamlit dashboard for visualizing credit risk metrics such as ECL by credit score band, PD vs EAD, and key portfolio KPIs.
Uses cleaned and enriched data from previous steps.
"""

# Load data
df = pd.read_csv('../data/final_dashboard_data.csv')

st.title("Credit Risk Modeling Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
credit_band = st.sidebar.multiselect("Credit Score Band", df['CreditScoreBand'].unique(), default=df['CreditScoreBand'].unique())
stage_filter = st.sidebar.multiselect("IFRS 9 Stage", df['IFRS9_Stage'].unique(), default=df['IFRS9_Stage'].unique())

filtered_df = df[df['CreditScoreBand'].isin(credit_band) & df['IFRS9_Stage'].isin(stage_filter)]

st.markdown("### Portfolio Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Loans", f"{len(filtered_df):,}")
col2.metric("Total ECL", f"€{filtered_df['ECL'].sum():,.2f}")
col3.metric("Avg. PD", f"{filtered_df['PD'].mean()*100:.2f}%")

fig1 = px.bar(filtered_df.groupby('CreditScoreBand')['ECL'].sum().reset_index(),
              x='CreditScoreBand', y='ECL', title='ECL by Credit Score Band',
              labels={'ECL': 'Expected Credit Loss (€)'})
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.scatter(filtered_df, x='PD', y='EAD', color='IFRS9_Stage',
                  size='ECL', hover_data=['CreditScore', 'LoanAmount'],
                  title='PD vs EAD (bubble size = ECL)')
st.plotly_chart(fig2, use_container_width=True)
