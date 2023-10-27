from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.write("# Forest Fever 🌳")

tab1, tab2, tab3 = st.tabs(["landing page", "interactive map", "abaout us"])

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


    with st.echo(code_location='below'):

        Point = namedtuple('Point', 'x y')
        data = []

        points_per_turn = total_points / num_turns

        for curr_point_num in range(total_points):
            curr_turn, i = divmod(curr_point_num, points_per_turn)
            angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
            radius = curr_point_num / total_points
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            data.append(Point(x, y))

        st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
            .mark_circle(color='#0068c9', opacity=0.5)
            .encode(x='x:Q', y='y:Q'))
