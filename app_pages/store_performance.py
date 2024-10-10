import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set the option to opt-in to the future behavior

df = pd.read_csv('outputs/Cleaned.csv')

def weekly_sales_by_dept(df):
    st.title('Weekly Sales by Department')
    sales_by_dept = df.groupby('Dept').sum()['Weekly_Sales'].reset_index()
    fig = px.bar(sales_by_dept, x='Dept', y='Weekly_Sales', title='Weekly Sales by Department')
    st.plotly_chart(fig)

def weekly_sales_line(df):
    st.title('Sales Forecast')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.strftime('%Y-%m')
    sales_by_month = df.groupby('Date').sum()['Weekly_Sales'].reset_index()
    
    # Convert Date to a numerical format
    sales_by_month['Date_Num'] = pd.to_datetime(sales_by_month['Date']).map(pd.Timestamp.toordinal)
    
    plt.figure(figsize=(10, 6))
    
    # Create the line plot with seaborn and add a trendline
    sns.lineplot(data=sales_by_month, x='Date_Num', y='Weekly_Sales', label='Weekly Sales')
    sns.regplot(data=sales_by_month, x='Date_Num', y='Weekly_Sales', scatter=False, label='Trendline', color='red')
    
    plt.title('Weekly Sales with Trendline')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.legend()
    st.pyplot(plt)

def markdown_multiline(df):
    st.title('Markdown Multiline Plot')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.strftime('%Y-%m')
    
    # Group by month and sum the values for each Markdown column
    markdown_cols = ['MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5']
    markdown_by_month = df.groupby('Month')[markdown_cols].sum().reset_index()
    
    plt.figure(figsize=(12, 8))
    
    for col in markdown_cols:
        sns.lineplot(data=markdown_by_month, x='Month', y=col, label=col)
    
    plt.title('Markdown Values Over Time')
    plt.xlabel('Month')
    plt.ylabel('Markdown Value')
    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot(plt)


def store_performance():
    st.title('Dashboard')
    st.write('This is the dashboard page')
    st.write('Scatter plot of age, bmi and charges')
    store_input = st.sidebar.selectbox("Store", options=range(0, 45))
    store_filter = df["Store"] > store_input
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.strftime('%Y')
    year_options = ['All Years'] + df['Date'].unique().tolist()
    year_input = st.sidebar.selectbox("Year", options=year_options)
    
    # Adjust filter logic
    if year_input == 'All Years':
        year_filter = df['Date'].isin(df['Date'].unique())
    else:
        year_filter = df['Date'] == year_input
    df_filter = df.loc[store_filter & year_filter]
    weekly_sales_by_dept(df_filter)
    weekly_sales_line(df_filter)
    markdown_multiline(df_filter)