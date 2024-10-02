import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set the option to opt-in to the future behavior

df = pd.read_csv('outputs/Cleaned.csv')

def sales_by_month(df):
    st.title('Sales by Month')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.strftime('%Y-%m')
    sales_by_month = df.groupby('Date').sum()['Weekly_Sales'].reset_index()
    fig = px.line(sales_by_month, x='Date', y='Weekly_Sales', title='Sales by Month')
    st.plotly_chart(fig)

def dashboard():
    st.title('Dashboard')
    st.write('This is the dashboard page')
    st.write('Scatter plot of age, bmi and charges')
    store_input = st.sidebar.select_slider("Store", options=range(0, 45))
    store_filter = df["Store"] > store_input
    df_filter = df.loc[store_filter]
    sales_by_month(df_filter)