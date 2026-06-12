import streamlit as st
from utils.data_manager import get_data
from utils.business_engine import business_score
from utils.business_engine import business_score

st.title("📈 Data Analysis Center")

df = get_data()

st.success("Dataset Loaded Successfully ✅")

st.markdown("---")

# Basic Information

st.subheader("📋 Dataset Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

with col3:
    st.metric("Missing Values", df.isnull().sum().sum())

st.markdown("---")

# Data Types

st.subheader("🧩 Data Types")

st.dataframe(df.dtypes.astype(str))

st.markdown("---")

# Missing Values

st.subheader("❓ Missing Values")

missing = df.isnull().sum()

st.dataframe(missing)

st.markdown("---")

# Duplicate Records

duplicates = df.duplicated().sum()

st.subheader("📑 Duplicate Records")

st.write("Duplicate Rows :", duplicates)

st.markdown("---")

# Statistical Summary

st.subheader("📊 Statistical Summary")

st.dataframe(df.describe())

st.markdown("---")

# Data Preview

st.subheader("👀 Dataset Preview")

st.dataframe(df)
st.markdown("---")

st.subheader("🏆 Data Quality Score")

score = business_score(df)

st.metric(
    "Business Score",
    f"{score}/100"
)

if score > 90:
    st.success("Excellent Dataset")
elif score > 70:
    st.warning("Good Dataset")
else:
    st.error("Poor Dataset")