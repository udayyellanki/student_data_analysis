import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")
st.title("📊 Student Performance Analysis")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("StudentsPerformance.csv")

df = load_data()

# Sidebar Filters
st.sidebar.header("Filter Student Data")
gender = st.sidebar.multiselect("Select Gender", options=df["gender"].unique(), default=df["gender"].unique())
prep = st.sidebar.multiselect("Test Preparation", options=df["test preparation course"].unique(), default=df["test preparation course"].unique())
parent_edu = st.sidebar.multiselect("Parental Level of Education", options=df["parental level of education"].unique(), default=df["parental level of education"].unique())

filtered_df = df[
    (df["gender"].isin(gender)) &
    (df["test preparation course"].isin(prep)) &
    (df["parental level of education"].isin(parent_edu))
]

# Show data preview
st.subheader("Filtered Data Preview")
st.dataframe(filtered_df.head())

# Visualizations
st.subheader("🎯 Score Distributions by Subject")

fig, ax = plt.subplots(1, 3, figsize=(20, 5))
sns.histplot(filtered_df["math score"], kde=True, ax=ax[0], color="skyblue")
ax[0].set_title("Math Score")

sns.histplot(filtered_df["reading score"], kde=True, ax=ax[1], color="lightgreen")
ax[1].set_title("Reading Score")

sns.histplot(filtered_df["writing score"], kde=True, ax=ax[2], color="salmon")
ax[2].set_title("Writing Score")

st.pyplot(fig)

# Correlation Matrix
st.subheader("📈 Correlation Heatmap")
corr = filtered_df[["math score", "reading score", "writing score"]].corr()

fig2, ax2 = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax2)
st.pyplot(fig2)

# Key Insights
st.subheader("🔍 Key Insights")
st.markdown("""
- 💡 Students who completed the test preparation course perform significantly better.
- 👨‍🎓 Parental education level positively correlates with student scores.
- 📘 Reading and writing scores have the strongest correlation.
""")

# Download data
st.download_button("Download Filtered Data", filtered_df.to_csv(index=False), file_name="filtered_student_data.csv")

# Footer
st.markdown("---")
st.caption("Created by Uday | Powered by Streamlit")
