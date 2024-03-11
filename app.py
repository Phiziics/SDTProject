import streamlit as st
import pandas as pd
import plotly.express as px

# Importing df
df = pd.read_csv('vehicles_us.csv')
# Remove rows with NaN values in'model_year', and 'model' columns in the original DataFrame
df.dropna(subset=['model_year', 'model','odometer'], inplace=True)
#Create the Make column
df['make'] = df['model'].str.split(' ').str[0]
#Update maodel column
df['model'] = df['model'].str.split(' ').str[1]
#4wd column adjustment
df['is_4wd'] = df['is_4wd'].fillna(0)
# Convert 'is_4wd' and 'model_year' columns to integer type
df[['is_4wd', 'model_year']] = df[['is_4wd', 'model_year']].astype(int)
grouped_df = df.groupby(['make', 'type']).size().reset_index(name='count')
# Replace NaN values in 'type' column with a default value
grouped_df['type'] = grouped_df['type'].fillna('Unknown')





# Header Streamlit app
st.header("Vehicle Analysis Dashboard")

# Create a histogram using Plotly Express
fig_histogram = px.histogram(df, x='model_year', color='condition', title='Distribution of Model Year by Condition', labels={'model_year': 'Model Year', 'condition': 'Condition'})
st.plotly_chart(fig_histogram)

# Create a scatter plot using Plotly Express
fig_scatter = px.scatter(df, x='odometer', y='price', color='make', title='Scatter Plot: Mileage vs. Price', labels={'odometer': 'Mileage', 'price': 'Price', 'make': 'Vehicle Make'})
st.plotly_chart(fig_scatter)
show_scatter = st.checkbox("Show Scatter Plot", value=True)
if show_scatter:
    st.plotly_chart(fig_scatter)
