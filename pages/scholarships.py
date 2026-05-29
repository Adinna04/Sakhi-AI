import streamlit as st
from config import SCHOLARSHIPS


def render_scholarships():
    st.markdown(
        '<div style="font-family:Poppins; font-size:1.8em; font-weight:800; color:white; margin-bottom:4px;">🎓 Scholarship Finder</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div style="color:rgba(255,255,255,0.5); margin-bottom:24px;">Apni padhai ke liye funding dhundho 💫</div>',
        unsafe_allow_html=True,
    )

    # Filters
    st.markdown("### 🔍 Filter Scholarships")
    col1, col2, col3 = st.columns(3)
    with col1:
        state_filter = st.selectbox(
            "State",
            ["All India", "Maharashtra", "West Bengal", "Delhi", "Rajasthan", "Other"],
        )
    with col2:
        course_filter = st.selectbox(
            "Course type",
            [
                "Any",
                "School",
                "Undergraduate",
                "Postgraduate",
                "Engineering/Technology",
                "Medical",
            ],
        )
    with col3:
        income_filter = st.selectbox(
            "Family income",
            ["Any", "Below 1.2 LPA", "Below 2 LPA", "Below 3.5 LPA", "Below 8 LPA"],
        )

    # Filter logic
    filtered = SCHOLARSHIPS.copy()
    if state_filter != "All India":
        filtered = [s for s in filtered if s["state"] in [state_filter, "All India"]]
    if course_filter != "Any":
        filtered = [
            s
            for s in filtered
            if course_filter.lower() in s["course"].lower() or s["course"] == "Any"
        ]

    st.markdown(
        f'<div style="color:rgba(255,255,255,0.5); font-size:0.85em; margin:12px 0;">{len(filtered)} scholarships found</div>',
        unsafe_allow_html=True,
    )

    for s in filtered:
        st.markdown(
            f"""
        <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(124,58,237,0.2);
            border-radius:18px; padding:20px; margin-bottom:14px;
            border-left:4px solid #7C3AED; transition:all 0.3s;">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px;">
                <div style="font-weight:700; color:white; font-size:1em;">{s['name']}</div>
                <div style="background:linear-gradient(135deg,rgba(124,58,237,0.3),rgba(236,72,153,0.3));
                    border:1px solid rgba(124,58,237,0.4); border-radius:20px; padding:4px 14px;
                    font-size:0.8em; font-weight:700; color:white; white-space:nowrap;">{s['amount']}</div>
            </div>
            <div style="color:rgba(255,255,255,0.6); font-size:0.85em; margin-bottom:8px;">{s['for']}</div>
            <div style="display:flex; gap:12px; flex-wrap:wrap; margin-bottom:12px;">
                <span style="background:rgba(124,58,237,0.15); border-radius:8px; padding:3px 10px;
                    font-size:0.75em; color:#a78bfa;">📍 {s['state']}</span>
                <span style="background:rgba(236,72,153,0.15); border-radius:8px; padding:3px 10px;
                    font-size:0.75em; color:#f9a8d4;">🎓 {s['course']}</span>
                <span style="background:rgba(16,185,129,0.15); border-radius:8px; padding:3px 10px;
                    font-size:0.75em; color:#6ee7b7;">💰 {s['income']}</span>
            </div>
            <a href="{s['link']}" target="_blank"
                style="background:linear-gradient(135deg,#7C3AED,#EC4899); border-radius:8px;
                padding:8px 20px; font-size:0.82em; font-weight:600; color:white;
                text-decoration:none; display:inline-block;">Apply Now →</a>
        </div>
        """,
            unsafe_allow_html=True,
        )
