import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime, date, timedelta
from utils.period_calc import calculate_cycle, get_cycle_phase
from utils.data_store import add_mood, add_journal_entry


def render_health():
    st.markdown(
        '<div style="font-family:Poppins; font-size:1.8em; font-weight:800; color:white; margin-bottom:4px;">🏥 Health & Wellness</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div style="color:rgba(255,255,255,0.5); margin-bottom:24px;">Track your health, mood & wellness journey 🌸</div>',
        unsafe_allow_html=True,
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        ["🩸 Period Tracker", "🧠 Mood Journal", "💧 Water Tracker", "📖 PCOS Info"]
    )

    # ── TAB 1: PERIOD TRACKER ──────────────────────────────────────────────
    with tab1:
        st.markdown("### 🩸 Period Tracker")
        col1, col2 = st.columns([1, 1])
        with col1:
            last_period = st.date_input(
                "Last period start date",
                value=date.today() - timedelta(days=14),
                max_value=date.today(),
            )
            cycle_length = st.slider(
                "Cycle length (days)",
                21,
                35,
                st.session_state.period_data.get("cycle_length", 28),
            )
            period_length = st.slider("Period duration (days)", 3, 7, 5)
            symptoms = st.multiselect(
                "Current symptoms",
                [
                    "Cramps",
                    "Bloating",
                    "Headache",
                    "Fatigue",
                    "Mood swings",
                    "Back pain",
                    "Nausea",
                    "Spotting",
                ],
            )

            if st.button(
                "📅 Calculate My Cycle", type="primary", use_container_width=True
            ):
                last_dt = datetime.combine(last_period, datetime.min.time())
                st.session_state.period_data = {
                    "last_date": last_dt,
                    "cycle_length": cycle_length,
                    "symptoms": symptoms,
                }
                st.rerun()

        with col2:
            if st.session_state.period_data["last_date"]:
                data = calculate_cycle(
                    st.session_state.period_data["last_date"], cycle_length
                )
                phase, color, advice = get_cycle_phase(data["cycle_day"], cycle_length)

                st.markdown(
                    f"""
                <div style="background:rgba(236,72,153,0.12); border:1px solid rgba(236,72,153,0.3);
                    border-radius:20px; padding:24px; text-align:center; margin-bottom:16px;">
                    <div style="font-size:0.8em; color:rgba(255,255,255,0.4); margin-bottom:8px;">CURRENT PHASE</div>
                    <div style="font-size:1.4em; font-weight:700; color:white;">{phase}</div>
                    <div style="font-size:0.85em; color:rgba(255,255,255,0.6); margin-top:8px; font-style:italic;">{advice}</div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

                info_cols = st.columns(2)
                with info_cols[0]:
                    st.metric(
                        "📅 Next Period",
                        data["next_period"].strftime("%d %b"),
                        f"In {data['days_until_next']} days",
                    )
                    st.metric("🌟 Ovulation", data["ovulation"].strftime("%d %b"))
                with info_cols[1]:
                    st.metric(
                        "🌱 Fertile Window",
                        f"{data['fertile_start'].strftime('%d')}-{data['fertile_end'].strftime('%d %b')}",
                    )
                    st.metric("😔 PMS Starts", data["pms_start"].strftime("%d %b"))

                # Cycle visualization
                fig = go.Figure()
                phases = [
                    "Menstrual\n(Day 1-5)",
                    "Follicular\n(Day 6-13)",
                    "Ovulation\n(Day 14-16)",
                    "Luteal\n(Day 17-28)",
                ]
                colors = ["#EC4899", "#7C3AED", "#f59e0b", "#6366f1"]
                sizes = [5, 8, 3, 12]
                for i, (ph, cl, sz) in enumerate(zip(phases, colors, sizes)):
                    fig.add_trace(
                        go.Bar(
                            x=[ph], y=[sz], marker_color=cl, name=ph, showlegend=False
                        )
                    )
                fig.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font_color="white",
                    height=200,
                    margin=dict(t=10, b=10),
                    xaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
                    yaxis=dict(visible=False),
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("👆 Enter your last period date to see predictions!")

    # ── TAB 2: MOOD JOURNAL ──────────────────────────────────────────────
    with tab2:
        st.markdown("### 🧠 Mood Journal")
        col1, col2 = st.columns([1, 1])

        with col1:
            st.markdown("**Log Today's Mood**")
            mood = st.selectbox(
                "How are you feeling?",
                [
                    "😊 Khush",
                    "😍 Excited",
                    "😔 Udaas",
                    "😰 Anxious",
                    "😴 Tired",
                    "💪 Motivated",
                    "😤 Frustrated",
                    "🤒 Unwell",
                ],
            )
            note = st.text_area(
                "What's on your mind? (optional)",
                placeholder="Aaj ka din kaisa tha...",
                height=120,
            )
            if st.button("📝 Save Entry", type="primary", use_container_width=True):
                add_journal_entry(mood, note)
                add_mood(mood, note)
                st.success("Journal entry saved! 💙")
                st.rerun()

        with col2:
            if st.session_state.journal_entries:
                st.markdown("**Recent Entries**")
                for entry in reversed(st.session_state.journal_entries[-5:]):
                    st.markdown(
                        f"""
                    <div style="background:rgba(255,255,255,0.04); border-radius:12px; padding:12px;
                        margin-bottom:8px; border-left:3px solid #7C3AED;">
                        <div style="font-size:0.75em; color:rgba(255,255,255,0.4);">{entry['date']}</div>
                        <div style="font-size:1.1em; margin:4px 0;">{entry['mood']}</div>
                        {f'<div style="font-size:0.85em; color:rgba(255,255,255,0.6);">{entry["note"]}</div>' if entry['note'] else ''}
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )

        # Mood chart
        if len(st.session_state.mood_history) >= 3:
            st.markdown("**Mood Trends**")
            mood_map = {
                "😊 Khush": 8,
                "😍 Excited": 9,
                "💪 Motivated": 8,
                "😴 Tired": 4,
                "😤 Frustrated": 3,
                "😰 Anxious": 3,
                "😔 Udaas": 2,
                "🤒 Unwell": 2,
            }
            history = st.session_state.mood_history[-14:]
            dates = [e["date"].split()[0] for e in history]
            scores = [mood_map.get(e["mood"], 5) for e in history]
            fig = go.Figure()
            fig.add_trace(
                go.Scatter(
                    x=dates,
                    y=scores,
                    mode="lines+markers",
                    line=dict(color="#7C3AED", width=3),
                    marker=dict(color="#EC4899", size=8),
                    fill="tozeroy",
                    fillcolor="rgba(124,58,237,0.1)",
                )
            )
            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font_color="white",
                height=220,
                margin=dict(t=10, b=30),
                xaxis=dict(gridcolor="rgba(255,255,255,0.05)", tickangle=-45),
                yaxis=dict(gridcolor="rgba(255,255,255,0.05)", range=[0, 10]),
            )
            st.plotly_chart(fig, use_container_width=True)

    # ── TAB 3: WATER TRACKER ──────────────────────────────────────────────
    with tab3:
        st.markdown("### 💧 Water Tracker")
        col1, col2 = st.columns([1, 1])
        with col1:
            glasses = st.session_state.water_intake
            progress = min(glasses / 8, 1.0)
            color = "#10b981" if glasses >= 8 else "#7C3AED"
            st.markdown(
                f"""
            <div style="background:rgba(255,255,255,0.05); border-radius:20px; padding:24px; text-align:center;">
                <div style="font-size:3em; margin-bottom:8px;">💧</div>
                <div style="font-size:2.5em; font-weight:800; color:{color};">{glasses}/8</div>
                <div style="color:rgba(255,255,255,0.5); margin-bottom:16px;">glasses today</div>
                <div style="background:rgba(255,255,255,0.1); border-radius:10px; height:12px; overflow:hidden;">
                    <div style="background:linear-gradient(90deg,#7C3AED,#10b981); height:100%; width:{progress*100}%;
                        border-radius:10px; transition:width 0.5s;"></div>
                </div>
                <div style="font-size:0.8em; color:rgba(255,255,255,0.4); margin-top:8px;">
                    {'🎉 Goal reached!' if glasses >= 8 else f'{8-glasses} more glasses to go!'}
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )
            c1, c2, c3 = st.columns(3)
            with c1:
                if st.button("➕ Add Glass", use_container_width=True):
                    st.session_state.water_intake = min(glasses + 1, 15)
                    st.rerun()
            with c2:
                if st.button("➖ Remove", use_container_width=True):
                    st.session_state.water_intake = max(glasses - 1, 0)
                    st.rerun()
            with c3:
                if st.button("🔄 Reset", use_container_width=True):
                    st.session_state.water_intake = 0
                    st.rerun()
        with col2:
            st.markdown(
                """
            <div style="background:rgba(16,185,129,0.1); border:1px solid rgba(16,185,129,0.25);
                border-radius:18px; padding:20px;">
                <div style="font-weight:700; color:white; margin-bottom:12px;">💡 Hydration Tips</div>
                <div style="color:rgba(255,255,255,0.7); font-size:0.88em; line-height:1.8;">
                    🌅 Subah uthke 2 glass pani piyo<br>
                    🍋 Lemon water metabolism boost karta hai<br>
                    📱 Water reminder app use karo<br>
                    🥤 Meals ke saath 1 glass zarur piyo<br>
                    🏃 Exercise ke baad extra pani chahiye<br>
                    🌡️ Garmi mein 10+ glasses pino
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    # ── TAB 4: PCOS INFO ──────────────────────────────────────────────
    with tab4:
        st.markdown("### 🔬 PCOS Information")
        st.info(
            "ℹ️ Yeh sirf educational information hai. Apne doctor se consult zarur karein."
        )

        pcos_topics = [
            (
                "🤔 PCOS Kya Hai?",
                "Polycystic Ovary Syndrome ek hormonal disorder hai jo reproductive age ki women mein common hai. India mein ~10-15% women affect hain.",
            ),
            (
                "⚠️ Common Symptoms",
                "Irregular periods • Weight gain • Acne • Hair fall • Excess facial hair • Difficulty conceiving • Mood swings",
            ),
            (
                "🥗 Diet Tips",
                "Low GI foods khao • Sugar reduce karo • Whole grains prefer karo • Omega-3 fatty acids loh • Processed foods avoid karo • Green vegetables zyada khao",
            ),
            (
                "🏃 Exercise",
                "Daily 30-min walk • Yoga (Kapalbhati, Anulom Vilom) • Strength training • Swimming • Cycling • High-intensity intervals avoid karo",
            ),
            (
                "💊 Treatment",
                "Doctor se consult karein • Metformin common medicine hai • Lifestyle changes important hain • Regular monitoring zaroori • Don't self-medicate",
            ),
        ]

        for title, content in pcos_topics:
            with st.expander(title):
                st.markdown(
                    f'<div style="color:rgba(255,255,255,0.8); line-height:1.8; font-size:0.9em;">{content}</div>',
                    unsafe_allow_html=True,
                )
