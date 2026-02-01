import streamlit as st
import numpy as np

st.title("Hello, Streamlit!")
with st.sidebar:
    st.header("This is the sidebar")
    st.write("You can put widgets here.")
st.write("Hello, Hurray!, Streamlit!")
st.header("This is a header with :blue[divider]", divider ="rainbow")
st.markdown("This is Markdown!")
col1, col2 = st.columns(2)
with col1:
    x = st.slider("Choose an X value", 1, 100)
with col2:
    st.write("The valuer of :blue[X] is", x)
