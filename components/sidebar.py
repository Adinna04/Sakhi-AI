import streamlit as st
from config import PAGES, EMERGENCY_CONTACTS, APP_NAME


def render_sidebar():
    with st.sidebar:
        # Logo
        st.markdown(
            """
        <div style="text-align:center; padding: 20px 0 16px;">
            <div style="font-size:2.5em;">🌸</div>
            <div style="font-family:'Poppins',sans-serif; font-size:1.5em; font-weight:800;
                background: linear-gradient(135deg, #7C3AED, #EC4899);
                -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                Sakhi AI
            </div>
            <div style="font-size:0.75em; color:rgba(255,255,255,0.5); margin-top:4px;">
                Your Digital Saheli 💙
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()

        # Navigation
        st.markdown(
            '<p style="font-size:0.72em; color:rgba(255,255,255,0.4); letter-spacing:2px; text-transform:uppercase; margin-bottom:8px;">NAVIGATION</p>',
            unsafe_allow_html=True,
        )

        for label, page_id in PAGES.items():
            is_active = st.session_state.current_page == page_id
            btn_style = (
                "background: linear-gradient(135deg,rgba(124,58,237,0.5),rgba(236,72,153,0.5)) !important; color:white !important; border-color:rgba(124,58,237,0.5) !important;"
                if is_active
                else ""
            )
            if st.button(label, key=f"nav_{page_id}", use_container_width=True):
                st.session_state.current_page = page_id
                st.rerun()

        st.divider()

        # Mood display
        if st.session_state.current_mood:
            st.markdown(
                f"""
            <div style="background:rgba(124,58,237,0.15); border:1px solid rgba(124,58,237,0.3);
                border-radius:14px; padding:14px; margin-bottom:16px; text-align:center;">
                <div style="font-size:0.72em; color:rgba(255,255,255,0.5); margin-bottom:6px;">TODAY'S MOOD</div>
                <div style="font-size:1.5em;">{st.session_state.current_mood}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

        # Stats
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                f"""
            <div style="background:rgba(255,255,255,0.05); border-radius:12px; padding:12px; text-align:center;">
                <div style="font-size:1.4em; font-weight:700; color:#7C3AED;">🔥{st.session_state.streak}</div>
                <div style="font-size:0.7em; color:rgba(255,255,255,0.4);">Day Streak</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                f"""
            <div style="background:rgba(255,255,255,0.05); border-radius:12px; padding:12px; text-align:center;">
                <div style="font-size:1.4em; font-weight:700; color:#EC4899;">💯{st.session_state.wellness_score}</div>
                <div style="font-size:0.7em; color:rgba(255,255,255,0.4);">Wellness</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

        st.divider()

        # Emergency
        with st.expander("🆘 Emergency Helplines"):
            for contact in EMERGENCY_CONTACTS:
                st.markdown(
                    f"""
                <div style="background:rgba(255,255,255,0.04); border-radius:10px; padding:10px; margin:6px 0;
                    border-left:3px solid #EC4899;">
                    <div style="font-size:0.8em; color:#EC4899; font-weight:600;">{contact['name']}</div>
                    <div style="font-size:1.2em; font-weight:700; color:white; letter-spacing:1px;">{contact['number']}</div>
                    <div style="font-size:0.7em; color:rgba(255,255,255,0.4);">{contact['desc']}</div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

        st.markdown(
            """
        <div style="text-align:center; padding:12px 0; font-size:0.72em; color:rgba(255,255,255,0.25);">
            Made with 💜 for every Indian girl<br>Sakhi AI v2.0
        </div>
        """,
            unsafe_allow_html=True,
        )
