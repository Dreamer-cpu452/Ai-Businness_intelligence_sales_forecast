import streamlit as st

def get_data():

    if "data" not in st.session_state:
        st.session_state["data"] = None

    if st.session_state["data"] is None:
        st.warning("⚠ Please upload a dataset first.")
        st.stop()

    return st.session_state["data"]