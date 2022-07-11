from datetime import datetime
import streamlit as st

st.header("FooBar")

with st.form(key="profile_form"):
    # text box
    name = st.text_input("name")
    address = st.text_input("address")

    # radio button
    age_category = st.radio(
        "Age category",
        ("Child(Under 18)", "Adult(Over 18)")
    )

    # slider
    height = st.slider("height", min_value=10, max_value=300)

    # multi select
    hobby = st.multiselect(
        "Hobby",
        ("A", "B", "C", "D", "E")
    )

    # color picker
    color = st.color_picker("theme colour", "#000000")

    # date
    start_date = st.date_input(
        "Start date",
        datetime.now()
    )

    # check box
    mail_subscribe = st.checkbox("Subscribe mail magazine (commonly seen evil default value)", True)

    submit_button = st.form_submit_button("submit")
    cancel_button = st.form_submit_button("cancel")


if submit_button:
    st.text(f"Welcome, {name}-san. I sent something to {address}.")
    st.text(f"Age category: {age_category}")
    st.text(f"Height: {height}")
    st.text(f"Hobby: {', '.join(hobby)}")
    st.text(f"Mail subscribe: {mail_subscribe}")
    st.text(f"Theme colour: {color}")
    st.text(f"Start date: {start_date}")
