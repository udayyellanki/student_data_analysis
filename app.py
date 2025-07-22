import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Data Analysis", layout="wide")

# Title
st.title("🎓 Student Performance Analysis Dashboard")

# Upload CSV
st.sidebar.header("Upload CSV")
uploaded_file = st.sidebar.file_uploader("Upload your Student Dataset", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Data Preview
    st.subheader("📄 Dataset Overview")
    st.dataframe(df.head())

    # Data Info
    st.markdown("### 🧹 Data Cleaning & Preprocessing")
    st.write(f"Shape of dataset: {df.shape}")
    st.write("Missing values:")
    st.write(df.isnull().sum())

    # Fix column names (if needed)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # EDA Section
    st.subheader("🔍 Exploratory Data Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Gender Distribution")
        fig1, ax1 = plt.subplots()
        sns.countplot(data=df, x="gender", ax=ax1)
        st.pyplot(fig1)

    with col2:
        st.markdown("#### Test Preparation Course")
        fig2, ax2 = plt.subplots()
        sns.countplot(data=df, x="test_preparation_course", ax=ax2)
        st.pyplot(fig2)

    # Score Distribution
    st.markdown("### 📊 Score Distribution")

    col3, col4, col5 = st.columns(3)

    with col3:
        st.markdown("#### Math Score")
        fig3, ax3 = plt.subplots()
        sns.histplot(df["math_score"], kde=True, ax=ax3)
        st.pyplot(fig3)

    with col4:
        st.markdown("#### Reading Score")
        fig4, ax4 = plt.subplots()
        sns.histplot(df["reading_score"], kde=True, ax=ax4)
        st.pyplot(fig4)

    with col5:
        st.markdown("#### Writing Score")
        fig5, ax5 = plt.subplots()
        sns.histplot(df["writing_score"], kde=True, ax=ax5)
        st.pyplot(fig5)

    # Correlation
    st.markdown("### 📈 Correlation Heatmap")
    fig6, ax6 = plt.subplots()
    sns.heatmap(df[["math_score", "reading_score", "writing_score"]].corr(), annot=True, cmap="coolwarm", ax=ax6)
    st.pyplot(fig6)

    # Boxplots
    st.markdown("### 📦 Boxplots by Gender")

    col6, col7, col8 = st.columns(3)

    with col6:
        fig7, ax7 = plt.subplots()
        sns.boxplot(data=df, x="gender", y="math_score", ax=ax7)
        ax7.set_title("Math Score")
        st.pyplot(fig7)

    with col7:
        fig8, ax8 = plt.subplots()
        sns.boxplot(data=df, x="gender", y="reading_score", ax=ax8)
        ax8.set_title("Reading Score")
        st.pyplot(fig8)

    with col8:
        fig9, ax9 = plt.subplots()
        sns.boxplot(data=df, x="gender", y="writing_score", ax=ax9)
        ax9.set_title("Writing Score")
        st.pyplot(fig9)

    # Filters
    st.markdown("### 🧪 Interactive Filters")

    gender_filter = st.selectbox("Select Gender", options=["All"] + list(df["gender"].unique()))
    lunch_filter = st.selectbox("Select Lunch Type", options=["All"] + list(df["lunch"].unique()))

    filtered_df = df.copy()
    if gender_filter != "All":
        filtered_df = filtered_df[filtered_df["gender"] == gender_filter]
    if lunch_filter != "All":
        filtered_df = filtered_df[filtered_df["lunch"] == lunch_filter]

    st.markdown("### 🎯 Filtered Data")
    st.dataframe(filtered_df)

    st.markdown("### 📌 Key Insights")
    st.markdown("""
    - Females often perform better in reading and writing.
    - Completion of the test preparation course improves scores.
    - There's a strong positive correlation between reading and writing scores.
    - Standard lunch students score better on average.
    """)

else:
    st.info("👈 Upload a CSV file to get started.")
