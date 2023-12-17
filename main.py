import numpy as np
import pandas as pd
import streamlit as st

st.title('10 minute to Pandas')

s = pd.Series([1, 3, 5, np.nan, 6, 8])
st.write(s)

dates = pd.date_range("20130101", periods=6)
st.write(dates)
