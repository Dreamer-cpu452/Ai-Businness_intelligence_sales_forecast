import streamlit as st
import pandas as pd

st.title("📂 Upload Sales Dataset")

st.write("Upload your sales dataset to begin analysis.")

uploaded_file = st.file_uploader(
    "Choose a CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Store dataset globally
    st.session_state["data"] = df

    st.success("✅ Dataset Uploaded Successfully!")

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

else:
    st.info("Please upload a dataset.")