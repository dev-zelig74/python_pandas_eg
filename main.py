import numpy as np
import pandas as pd
import streamlit as st

s = pd.Series([1, 3, 5, np.nan, 6, 8])
st.print(s)
