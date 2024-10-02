import streamlit as st  # Importing the Streamlit library
from app_pages.multi_page import MultiPage  # Importing the MultiPage class from app_pages.multi_page module
from app_pages.dashboard import dashboard 
from app_pages.store_performance import store_performance
 
app = MultiPage(app_name="Dashboard App")  
app.add_page("Retail Sales Predictions", dashboard)
app.add_page("Store Department Overview", store_performance)

app.run()  # Running the MultiPage app