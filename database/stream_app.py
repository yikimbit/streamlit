import streamlit as st

conn = st.connection("my_database")
df = conn.query("select * from job_point_ht")
st.dataframe(df)