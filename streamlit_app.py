import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime, timedelta

st.write("# Forest Fever 🌳")

tab1, tab2, tab3 = st.tabs(["landing page", "interactive map", "about us"])

with tab1:
    # Using object notation
    # Erstelle einen Date/Time-Schieberegler mit einem Wochenbereich
    start_date = datetime(2020, 1, 1)
    end_date = start_date + timedelta(weeks=1)
    
    selected_date = st.slider(
        "Wählen Sie einen Datumsbereich",
        min_value=start_date,
        max_value=end_date,
        value=(start_date, end_date),
        step=timedelta(days=1),
    )
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
        st.button("Reset", type="primary")
        if st.button('Say hello'):
            st.write('Why hello there')
        else:
            st.write('Goodbye')

with tab2:
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(df)
