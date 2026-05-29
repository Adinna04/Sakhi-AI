import streamlit as st
from utils.ai_helper import get_career_roadmap


def render_career():
    st.markdown(
        '<div style="font-family:Poppins; font-size:1.8em; font-weight:800; color:white; margin-bottom:4px;">💼 Career Coach</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div style="color:rgba(255,255,255,0.5); margin-bottom:24px;">Apna dream career achieve karo — Sakhi hai tumhare saath 🚀</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### 🎯 Get Your Career Roadmap")
        course = st.selectbox(
            "Your current course/degree",
            [
                "B.Tech / B.E.",
                "BCA / MCA",
                "B.Sc",
                "B.Com / M.Com",
                "BA / MA",
                "MBA",
                "MBBS / Medical",
                "Law",
                "Design",
                "Other",
            ],
        )
        year = st.selectbox(
            "Current year",
            ["1st Year", "2nd Year", "3rd Year", "4th Year", "Final Year", "Graduate"],
        )
        goal = st.text_input(
            "Career goal",
            placeholder="e.g. Software Engineer at Google, UX Designer, IAS Officer...",
        )
        skills = st.multiselect(
            "Skills you already have",
            [
                "Python",
                "Java",
                "JavaScript",
                "React",
                "SQL",
                "Excel",
                "Communication",
                "Leadership",
                "Design",
                "Marketing",
                "Content Writing",
            ],
        )
        if st.button(
            "🚀 Generate My Roadmap", type="primary", use_container_width=True
        ):
            if goal:
                with st.spinner("Sakhi tera roadmap bana rahi hai... 🗺️"):
                    result = get_career_roadmap(course, year, goal)
                st.session_state["career_roadmap"] = result
                st.rerun()
            else:
                st.warning("Apna career goal enter karo!")

    with col2:
        if "career_roadmap" in st.session_state:
            st.markdown("### 📋 Your Personalized Roadmap")
            st.markdown(
                f"""
            <div style="background:rgba(124,58,237,0.1); border:1px solid rgba(124,58,237,0.25);
                border-radius:18px; padding:20px; max-height:500px; overflow-y:auto;">
                <div style="color:rgba(255,255,255,0.85); line-height:1.9; font-size:0.88em;">
                    {st.session_state['career_roadmap'].replace(chr(10), '<br>')}
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
            <div style="background:rgba(255,255,255,0.04); border:1px dashed rgba(255,255,255,0.15);
                border-radius:18px; padding:40px; text-align:center;">
                <div style="font-size:3em; margin-bottom:12px;">🗺️</div>
                <div style="color:rgba(255,255,255,0.4); font-size:0.9em;">
                    Fill in the form and click Generate to see your personalized career roadmap
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.divider()

    # Career Resources
    st.markdown("### 📚 Top Free Resources")
    resources = [
        ("🎓", "Coursera", "Free courses with certificates", "https://coursera.org"),
        ("🛠️", "freeCodeCamp", "Free coding bootcamp", "https://freecodecamp.org"),
        ("💻", "Internshala", "Internships for students", "https://internshala.com"),
        (
            "🌐",
            "LinkedIn Learning",
            "Professional skills",
            "https://linkedin.com/learning",
        ),
        ("🏆", "HackerRank", "Coding practice & jobs", "https://hackerrank.com"),
        ("📊", "NPTEL", "Free IIT/IISc courses", "https://nptel.ac.in"),
    ]
    res_cols = st.columns(3)
    for i, (icon, name, desc, link) in enumerate(resources):
        with res_cols[i % 3]:
            st.markdown(
                f"""
            <div style="background:rgba(255,255,255,0.05); border-radius:14px; padding:16px; margin-bottom:12px;
                border:1px solid rgba(255,255,255,0.08);">
                <div style="font-size:1.5em; margin-bottom:6px;">{icon}</div>
                <div style="font-weight:700; color:white; font-size:0.9em;">{name}</div>
                <div style="font-size:0.78em; color:rgba(255,255,255,0.5); margin:4px 0;">{desc}</div>
                <a href="{link}" target="_blank" style="font-size:0.78em; color:#7C3AED; text-decoration:none;">Visit →</a>
            </div>
            """,
                unsafe_allow_html=True,
            )
