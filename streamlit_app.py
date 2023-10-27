import pandas as pd
import streamlit as st
import numpy as np

st.write("# Forest Fever 🌳")

tab1, tab2, tab3 = st.tabs(["landing page", "interactive map", "about us"])

with tab1:
    # Using object notation
    total_points = st.sidebar.slider("date", 1, 5000, 2000)
    num_turns = st.sidebar.slider("bsome bullshit", 1, 100, 9)

    add_selectbox = st.sidebar.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone")
    )

    # Using "with" notation
    with st.sidebar:
        add_radio = st.radio(
            "Choose a indicator",
            ("dry", "wet", "ligma")
        )

    with st.sidebar:
        darmstadt = st.button(
            "centralize"
        )
        
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(df)
