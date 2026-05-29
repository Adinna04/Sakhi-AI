import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
from utils.data_store import update_wellness_score


def render_profile():
    st.markdown(
        '<div style="font-family:Poppins; font-size:1.8em; font-weight:800; color:white; margin-bottom:24px;">👤 My Profile</div>',
        unsafe_allow_html=True,
    )

    update_wellness_score()

    col1, col2 = st.columns([1, 2])
    with col1:
        name = st.text_input(
            "Your name", value=st.session_state.username, placeholder="Enter your name"
        )
        if name != st.session_state.username:
            st.session_state.username = name

        st.markdown(
            f"""
        <div style="background:linear-gradient(135deg,rgba(124,58,237,0.2),rgba(236,72,153,0.2));
            border:1px solid rgba(124,58,237,0.3); border-radius:20px; padding:24px; text-align:center; margin:16px 0;">
            <div style="font-size:3em; margin-bottom:8px;">👸</div>
            <div style="font-family:Poppins; font-size:1.2em; font-weight:700; color:white;">{st.session_state.username}</div>
            <div style="font-size:0.8em; color:rgba(255,255,255,0.5); margin-top:4px;">Sakhi Member</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # Stats
        stats = [
            ("🔥", "Day Streak", st.session_state.streak),
            ("💯", "Wellness Score", f"{st.session_state.wellness_score}/100"),
            ("📝", "Journal Entries", len(st.session_state.journal_entries)),
            ("💬", "Chats Saved", len(st.session_state.saved_chats)),
        ]
        for icon, label, val in stats:
            st.markdown(
                f"""
            <div style="background:rgba(255,255,255,0.05); border-radius:12px; padding:12px 16px;
                margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:0.85em; color:rgba(255,255,255,0.6);">{icon} {label}</span>
                <span style="font-weight:700; color:white;">{val}</span>
            </div>
            """,
                unsafe_allow_html=True,
            )

    with col2:
        # Wellness gauge
        st.markdown("### 💯 Wellness Score")
        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=st.session_state.wellness_score,
                domain={"x": [0, 1], "y": [0, 1]},
                title={
                    "text": "Overall Wellness",
                    "font": {"color": "white", "size": 16},
                },
                number={"font": {"color": "white", "size": 40}},
                gauge={
                    "axis": {"range": [0, 100], "tickcolor": "rgba(255,255,255,0.3)"},
                    "bar": {"color": "#7C3AED"},
                    "bgcolor": "rgba(0,0,0,0)",
                    "bordercolor": "rgba(255,255,255,0.1)",
                    "steps": [
                        {"range": [0, 33], "color": "rgba(239,68,68,0.2)"},
                        {"range": [33, 66], "color": "rgba(245,158,11,0.2)"},
                        {"range": [66, 100], "color": "rgba(16,185,129,0.2)"},
                    ],
                    "threshold": {
                        "line": {"color": "#EC4899", "width": 3},
                        "thickness": 0.75,
                        "value": st.session_state.wellness_score,
                    },
                },
            )
        )
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="white",
            height=280,
            margin=dict(t=40, b=10),
        )
        st.plotly_chart(fig, use_container_width=True)

        # Achievements
        st.markdown("### 🏆 Achievements")
        achievements_all = [
            (
                "🌟",
                "First Chat",
                len(st.session_state.messages) > 0,
                "Had your first Sakhi chat",
            ),
            (
                "💧",
                "Hydration Hero",
                st.session_state.water_intake >= 8,
                "Drank 8 glasses of water",
            ),
            (
                "📝",
                "Journal Starter",
                len(st.session_state.journal_entries) >= 1,
                "Made first journal entry",
            ),
            ("🔥", "Week Warrior", st.session_state.streak >= 7, "7-day streak!"),
            (
                "😊",
                "Mood Tracker",
                len(st.session_state.mood_history) >= 5,
                "Tracked mood 5 times",
            ),
            (
                "💬",
                "Conversation Queen",
                len(st.session_state.saved_chats) >= 1,
                "Saved a conversation",
            ),
        ]
        ach_cols = st.columns(3)
        for i, (icon, name, earned, desc) in enumerate(achievements_all):
            with ach_cols[i % 3]:
                opacity = "1" if earned else "0.3"
                bg = "rgba(124,58,237,0.2)" if earned else "rgba(255,255,255,0.04)"
                st.markdown(
                    f"""
                <div style="background:{bg}; border-radius:14px; padding:14px; text-align:center;
                    opacity:{opacity}; margin-bottom:10px; border:1px solid rgba(124,58,237,{'0.4' if earned else '0.1'});">
                    <div style="font-size:1.8em;">{icon}</div>
                    <div style="font-weight:600; color:white; font-size:0.78em; margin-top:4px;">{name}</div>
                    <div style="font-size:0.68em; color:rgba(255,255,255,0.4);">{desc}</div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

    # Saved Chats
    if st.session_state.saved_chats:
        st.divider()
        st.markdown("### 💬 Saved Chats")
        for chat in reversed(st.session_state.saved_chats[-5:]):
            with st.expander(f"{chat['mode']} — {chat['date']}"):
                for msg in chat["messages"][-4:]:
                    role_icon = "🌸" if msg["role"] == "assistant" else "👤"
                    st.markdown(
                        f"**{role_icon}**: {msg['content'][:200]}{'...' if len(msg['content']) > 200 else ''}"
                    )
