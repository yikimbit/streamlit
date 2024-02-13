import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(10, 2) / [50, 50] + [35.03, 126.78],
    columns=['lat', 'lon'])
st.dataframe(map_data)
st.map(map_data)