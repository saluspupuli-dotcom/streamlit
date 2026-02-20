import streamlit as st
from PIL import Image

# Page config
st.set_page_config(
    page_title="My Portfolio",
    page_icon="🎨",
    layout="wide"
)

# Load images
profile_image = Image.open("profile.jpg")
project_image = Image.open("timenest.png")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Me", "Skills", "Portfolio", "Contact"])

# Pages
if page == "About Me":
    st.title("👋 Hello! I'm Felix Eupena")
    st.subheader("IT Student | Aspiring Developer | Creative Thinker")
    st.write("Welcome to my personal portfolio and autobiography!")

    st.header("About Me")
    st.write("""
    Hi, I'm Felix Eupena, an IT student passionate about web development, 
    database design, and creating digital solutions that help people. 
    I enjoy learning new technologies and working on projects that challenge my skills.
    """)
    st.image(profile_image, caption="Me at my favorite coding spot", width=250)

elif page == "Skills":
    st.header("Skills")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Python")
        st.progress(80)
    with col2:
        st.subheader("Web Development")
        st.progress(70)
    with col3:
        st.subheader("Database Management")
        st.progress(75)

elif page == "Portfolio":
    st.header("Projects")
    st.subheader("Time Nest - Web App for Students")
    st.write("A web app to manage student schedules, tasks, and time management.")
    st.image(project_image, width=400)

elif page == "Contact":
    st.header("Contact Me")
    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send")
    if submit_button:
        st.success(f"Thanks {name}, your message has been sent!")
        st.balloons()

