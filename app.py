import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("Nifty_Stocks.csv")
df['Date'] = pd.to_datetime(df['Date'])

st.title("📈 Nifty Stock Price Visualizer")

# Sidebar filters
st.sidebar.header("Filter Options")

# Category selection
categories = df['Category'].unique()
selected_category = st.sidebar.selectbox("Select Category", categories)

# Filter by selected category
filtered_df = df[df['Category'] == selected_category]

# Symbol selection
symbols = filtered_df['Symbol'].unique()
selected_symbol = st.sidebar.selectbox("Select Stock", symbols)

# Filter by selected symbol
stock_df = filtered_df[filtered_df['Symbol'] == selected_symbol]

# Plotting
st.subheader(f"Closing Prices of {selected_symbol} in Category: {selected_category}")

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=stock_df, x='Date', y='Close', ax=ax)
ax.set_title(f"{selected_symbol} Stock Price Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Close Price")

st.pyplot(fig)
