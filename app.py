import matplotlib.font_manager as fm
import streamlit as st

font_names = sorted({f.name for f in fm.fontManager.ttflist})
st.write(font_names)
