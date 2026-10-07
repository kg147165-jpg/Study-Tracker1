import streamlit as st

from database import create_database, create_user, verify_user


create_database()

st.set_page_config(
    page_title="Study Tracker",
    page_icon="📚"
)

st.title("📚 Study Tracker")

st.write("Your personal study tracking system.")


option = st.radio(
    "Choose an option:",
    ["Login", "Sign Up"]
)


if option == "Sign Up":

    st.header("Create your account")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button("Create Account"):

        if not username or not password:
            st.error("Please enter a username and password.")

        elif password != confirm_password:
            st.error("Passwords do not match.")

        else:
            try:
                create_user(username, password)
                st.success("Account created successfully!")

            except Exception:
                st.error("That username may already exist.")


if option == "Login":

    st.header("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        user = verify_user(username, password)

        if user:
            st.success(f"Welcome, {user[1]}!")

        else:
            st.error("Invalid username or password.")