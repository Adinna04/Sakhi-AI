import streamlit as st

# Page config MUST be first
st.set_page_config(
    page_title="Sakhi AI — Har Ladki Ki Digital Saheli",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Init session state
from utils.data_store import init_session_state

init_session_state()

# Render sidebar
from components.sidebar import render_sidebar

render_sidebar()

# Route to pages
page = st.session_state.current_page

if page == "home":
    from pages.home import render_home

    render_home()
elif page == "chat":
    from pages.chat import render_chat

    render_chat()
elif page == "health":
    from pages.health import render_health

    render_health()
elif page == "safety":
    from pages.safety import render_safety

    render_safety()
elif page == "profile":
    from pages.profile import render_profile

    render_profile()
elif page == "scholarships":
    from pages.scholarships import render_scholarships

    render_scholarships()
elif page == "career":
    from pages.career import render_career

    render_career()
