import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime, timedelta
from PIL import Image
import pydeck as pdk

st.write("# CanopyAI 🌳👑")

tab1, tab2, tab3 = st.tabs(["landing page", "interactive map", "about us"])

with tab1:
    # Using object notation
    # Erstelle einen Date/Time-Schieberegler mit einem Wochenbereich
    start_date = datetime(2020, 1, 1)
    end_date = start_date + timedelta(weeks=100)

    selected_date = st.sidebar.slider(
        "Select a date range",
        min_value=start_date,
        max_value=end_date,
        value=(start_date, end_date),
        step=timedelta(days=1),
    )
    num_turns = st.sidebar.slider("some bullshit", 1, 100, 9)

    add_selectbox = st.sidebar.selectbox(
        "Background map",
        ("default", "terrain", "satellite")
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
            pdk.View(
                longitude=8.65027, latitude=49.87167 , zoom=6, min_zoom=5, max_zoom=15, pitch=0, bearing=0
            )
            st.write('centralized to darmstadt')
        else:
            st.write('fuck off')

with tab2:
    UK_ACCIDENTS_DATA = (
        "https://raw.githubusercontent.com/uber-common/"
        "deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv"
    )
    layer = pdk.Layer(
        "HexagonLayer",
        UK_ACCIDENTS_DATA,
        get_position="[lng, lat]",
        auto_highlight=True,
        elevation_scale=50,
        pickable=True,
        elevation_range=[0, 3000],
        extruded=True,
        coverage=1,
    )
    # Set the viewport location
    view_state = pdk.ViewState(
        longitude=8.65027, latitude=49.87167 , zoom=3, min_zoom=5, max_zoom=15, pitch=0, bearing=0
    )
    # Combined all of it and render a viewport
    r = pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"html": "<b>Elevation Value:</b> {elevationValue}", "style": {"color": "white"}},
    )
    st.pydeck_chart(r)

with tab3:

    # col1, col2, col3 , col4, col5= st.columns(5, gap="large")

    st.header("Theo")
    theo = Image.open('./pics/theo.jpg').resize((400, 400))
    st.image(theo, caption='https://www.linkedin.com/in/theodor-nguyen-816269133/')

    st.header("Tim")
    tim = Image.open('./pics/tim.jpg').resize((400, 400))
    st.image(tim, caption='https://www.linkedin.com/in/tim%2Dvielhauer%2D66984026b/')

    st.header("Alfred")
    alfred = Image.open('./pics/alfred.jpg').resize((400, 400))
    st.image(alfred, caption='https://www.linkedin.com/in/alfred-quan-anh-nguyen/')

    st.header("Niclas")
    niclas = Image.open('./pics/niclas.jpg').resize((400, 400))
    st.image(niclas, caption='https://www.linkedin.com/in/niclas-schilling/')

    st.header("Benno")
    benno = Image.open('./pics/benno.jpg').resize((400, 400))
    st.image(benno, caption='https://www.linkedin.com/in/benno-koesters/')
    
