import streamlit as st
import random
from datetime import datetime
from config import DAILY_QUOTES, MOOD_OPTIONS, GOVERNMENT_SCHEMES
from utils.data_store import add_mood


def render_home():
    # Hero Section
    hour = datetime.now().hour
    greeting = (
        "Subah ki shubhkamnayein"
        if hour < 12
        else ("Good afternoon" if hour < 17 else "Good evening")
    )

    st.markdown(
        f"""
    <div style="background: linear-gradient(135deg, rgba(124,58,237,0.25) 0%, rgba(236,72,153,0.25) 100%);
        border: 1px solid rgba(124,58,237,0.3); border-radius: 28px; padding: 48px 32px;
        text-align: center; position: relative; overflow: hidden; margin-bottom: 28px;">
        <div style="font-size:0.9em; color:rgba(255,255,255,0.6); margin-bottom:8px; letter-spacing:1px;">{greeting} ☀️</div>
        <div style="font-family:'Poppins',sans-serif; font-size:2.8em; font-weight:800; color:white; margin:0; line-height:1.2;">
            Hi, I'm Sakhi 🌸
        </div>
        <div style="font-size:1.1em; color:rgba(255,255,255,0.7); margin:12px 0 24px; line-height:1.6;">
            Your AI Companion for Wellness, Safety & Growth
        </div>
        <div style="display:inline-block; background:linear-gradient(135deg,#7C3AED,#EC4899);
            border-radius:50px; padding:14px 40px; font-weight:700; font-size:1.05em;
            color:white; cursor:pointer; box-shadow:0 8px 32px rgba(124,58,237,0.4);">
            ✨ Talk to Sakhi
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Talk to Sakhi CTA button
    if st.button(
        "💬 Start Chatting with Sakhi", use_container_width=True, type="primary"
    ):
        st.session_state.current_page = "chat"
        st.rerun()

    # Mood Check-In
    st.markdown(
        """
    <div style="font-family:'Poppins',sans-serif; font-size:1.3em; font-weight:700;
        color:white; margin: 28px 0 16px;">
        💜 Aaj kaisa feel ho raha hai?
    </div>
    """,
        unsafe_allow_html=True,
    )

    mood_cols = st.columns(4)
    for i, mood in enumerate(MOOD_OPTIONS[:4]):
        with mood_cols[i]:
            if st.button(mood, key=f"mood_{i}", use_container_width=True):
                add_mood(mood)
                st.success(f"Noted! {mood} 💙")
                st.rerun()

    mood_cols2 = st.columns(4)
    for i, mood in enumerate(MOOD_OPTIONS[4:]):
        with mood_cols2[i]:
            if st.button(mood, key=f"mood2_{i}", use_container_width=True):
                add_mood(mood)
                st.success(f"Noted! {mood} 💙")
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Daily Quote
    quote = DAILY_QUOTES[datetime.now().day % len(DAILY_QUOTES)]
    st.markdown(
        f"""
    <div style="background: linear-gradient(135deg, rgba(124,58,237,0.15), rgba(236,72,153,0.15));
        border: 1px solid rgba(124,58,237,0.25); border-radius: 20px; padding: 24px;
        text-align: center; margin-bottom: 28px;">
        <div style="font-size:0.8em; color:rgba(255,255,255,0.4); letter-spacing:2px; margin-bottom:10px;">✨ DAILY INSPIRATION</div>
        <div style="font-size:1.2em; font-style:italic; color:white; line-height:1.7;">"{quote}"</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Quick Actions Grid
    st.markdown(
        '<div style="font-family:Poppins; font-size:1.3em; font-weight:700; color:white; margin-bottom:16px;">🚀 Quick Actions</div>',
        unsafe_allow_html=True,
    )

    actions = [
        ("🩸", "Period Tracker", "Track your cycle", "health"),
        ("🎓", "Scholarships", "Find funding", "scholarships"),
        ("💼", "Career Coach", "Plan your path", "career"),
        ("🛡️", "Safety Hub", "Stay protected", "safety"),
        ("⚖️", "Legal Rights", "Know your rights", "chat"),
        ("💰", "Finance Guide", "Money tips", "chat"),
        ("🧠", "Mood Journal", "Track emotions", "health"),
        ("📚", "Learning Hub", "Grow skills", "chat"),
    ]

    cols1 = st.columns(4)
    for i, (icon, title, subtitle, page) in enumerate(actions[:4]):
        with cols1[i]:
            st.markdown(
                f"""
            <div style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1);
                border-radius:20px; padding:20px 16px; text-align:center; cursor:pointer;
                transition:all 0.3s; margin-bottom:12px;"
                onmouseover="this.style.borderColor='rgba(124,58,237,0.5)'"
                onmouseout="this.style.borderColor='rgba(255,255,255,0.1)'">
                <div style="font-size:2em; margin-bottom:8px;">{icon}</div>
                <div style="font-weight:700; color:white; font-size:0.9em;">{title}</div>
                <div style="font-size:0.75em; color:rgba(255,255,255,0.4); margin-top:4px;">{subtitle}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
            if st.button(f"→ {title}", key=f"qa_{i}", use_container_width=True):
                st.session_state.current_page = page
                st.rerun()

    cols2 = st.columns(4)
    for i, (icon, title, subtitle, page) in enumerate(actions[4:]):
        with cols2[i]:
            st.markdown(
                f"""
            <div style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1);
                border-radius:20px; padding:20px 16px; text-align:center; cursor:pointer;
                transition:all 0.3s; margin-bottom:12px;">
                <div style="font-size:2em; margin-bottom:8px;">{icon}</div>
                <div style="font-weight:700; color:white; font-size:0.9em;">{title}</div>
                <div style="font-size:0.75em; color:rgba(255,255,255,0.4); margin-top:4px;">{subtitle}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
            if st.button(f"→ {title}", key=f"qa2_{i}", use_container_width=True):
                st.session_state.current_page = page
                st.rerun()

    # Government Schemes
    st.markdown(
        '<div style="font-family:Poppins; font-size:1.3em; font-weight:700; color:white; margin: 24px 0 16px;">🏛️ Government Schemes for Women</div>',
        unsafe_allow_html=True,
    )
    scheme_cols = st.columns(3)
    for i, scheme in enumerate(GOVERNMENT_SCHEMES):
        with scheme_cols[i % 3]:
            st.markdown(
                f"""
            <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08);
                border-radius:16px; padding:16px; margin-bottom:12px;
                border-left:3px solid #7C3AED;">
                <div style="font-weight:600; color:white; font-size:0.9em; margin-bottom:4px;">{scheme['name']}</div>
                <div style="font-size:0.78em; color:rgba(255,255,255,0.5);">{scheme['desc']}</div>
                <div style="font-size:0.7em; color:#7C3AED; margin-top:6px;">📋 {scheme['ministry']}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
