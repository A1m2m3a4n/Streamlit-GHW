import streamlit as st
import numpy as np
import pandas as pd
import csv

st.title('Pokemon Data Visualisation Tool')
st.divider()

# Load Data
def load_data():
    data = pd.read_csv('pokemon.csv')
    return data

data = load_data()

# Create a dataframe with the pokemon data
df = st.dataframe(data)

st.dataframe(df)