import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('StudentsPerformance.csv')

# Title
st.title("📊 Student Performance Analysis Dashboard")
st.markdown("Analyze student scores based on gender, lunch type, and more.")

# Filters
gender_filter = st.sidebar.multiselect("Select Gender", options=df['gender'].unique(), default=df['gender'].unique())
lunch_filter = st.sidebar.multiselect("Select Lunch Type", options=df['lunch'].unique(), default=df['lunch'].unique())

# Apply filters
filtered_df = df[(df['gender'].isin(gender_filter)) & (df['lunch'].isin(lunch_filter))]

# Show Data
with st.expander("📂 View Filtered Data"):
    st.dataframe(filtered_df)

# Top performers
st.subheader("🏅 Top 5 Students in Math")
top_math = filtered_df.sort_values(by='math score', ascending=False).head(5)
st.dataframe(top_math[['gender', 'math score', 'reading score', 'writing score']])

# Bar Chart - Average scores by gender
st.subheader("📊 Average Scores by Gender")
avg_scores = filtered_df.groupby('gender')[['math score', 'reading score', 'writing score']].mean().reset_index()
st.bar_chart(avg_scores.set_index('gender'))

# Score Distribution
st.subheader("🎯 Score Distribution")
fig, ax = plt.subplots(figsize=(10, 4))
sns.boxplot(data=filtered_df[['math score', 'reading score', 'writing score']], palette='Set3', ax=ax)
st.pyplot(fig)

# Scatter Plot
st.subheader("🔁 Reading vs Writing Score")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=filtered_df, x='reading score', y='writing score', hue='gender', ax=ax2)
st.pyplot(fig2)

# Footer
st.markdown("💡 *Built with Streamlit, Pandas, Seaborn*")
