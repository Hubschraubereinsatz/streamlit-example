import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime, timedelta
from PIL import Image

st.write("# Forest Fever 🌳")

tab1, tab2, tab3 = st.tabs(["landing page", "interactive map", "about us"])

with tab1:
    # Using object notation
    # Erstelle einen Date/Time-Schieberegler mit einem Wochenbereich
    start_date = datetime(2020, 1, 1)
    end_date = start_date + timedelta(weeks=100)

    selected_date = st.sidebar.slider(
        "Wählen Sie einen Datumsbereich",
        min_value=start_date,
        max_value=end_date,
        value=(start_date, end_date),
        step=timedelta(days=1),
    )
    num_turns = st.sidebar.slider("some bullshit", 1, 100, 9)

    add_selectbox = st.sidebar.selectbox(
        "Background map",
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
        if st.button('centralize '):
            st.write('centralized to darmstadt')
        else:
            st.write('fuck of')

with tab2:
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(df)


with tab3:
    theo = Image.open('./pics/theo.jpg')
    st.image(theo, caption='https://www.linkedin.com/in/theodor-nguyen-816269133/')

    alfred = Image.open('./pics/alfred.jpg')
    st.image(alfred, caption='https://www.linkedin.com/in/alfred-quan-anh-nguyen/')

    tim = Image.open('./pics/tim.jpg')
    st.image(tim, caption='https://www.linkedin.com/in/tim%2Dvielhauer%2D66984026b/')

    niclas = Image.open('./pics/niclas.jpg')
    st.image(niclas, caption='https://www.linkedin.com/in/niclas-schilling/')

    benno = Image.open('./pics/benno.jpg')
    st.image(benno, caption='https://www.linkedin.com/in/benno-koesters/')
