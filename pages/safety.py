import streamlit as st
from utils.ai_helper import analyze_scam
from config import EMERGENCY_CONTACTS


def render_safety():
    st.markdown(
        '<div style="font-family:Poppins; font-size:1.8em; font-weight:800; color:white; margin-bottom:4px;">🛡️ Safety Hub</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div style="color:rgba(255,255,255,0.5); margin-bottom:24px;">Tumhari suraksha hamaari pehli priority hai 💪</div>',
        unsafe_allow_html=True,
    )

    # SOS Section
    st.markdown(
        """
    <div style="background: linear-gradient(135deg, rgba(220,38,38,0.25), rgba(239,68,68,0.15));
        border: 1px solid rgba(239,68,68,0.4); border-radius: 24px; padding: 32px; text-align: center; margin-bottom: 28px;">
        <div style="font-size:2em; margin-bottom:8px;">🆘</div>
        <div style="font-family:Poppins; font-size:1.6em; font-weight:800; color:white; margin-bottom:8px;">Emergency SOS</div>
        <div style="color:rgba(255,255,255,0.6); margin-bottom:20px; font-size:0.95em;">
            Kisi bhi emergency mein in numbers pe call karo. Tum akeli nahi ho. 💙
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Emergency contacts grid
    ec_cols = st.columns(4)
    for i, contact in enumerate(EMERGENCY_CONTACTS[:4]):
        with ec_cols[i]:
            st.markdown(
                f"""
            <div style="background:rgba(220,38,38,0.12); border:1px solid rgba(220,38,38,0.3);
                border-radius:18px; padding:20px; text-align:center; margin-bottom:12px;">
                <div style="font-size:1.8em; margin-bottom:6px;">📞</div>
                <div style="font-weight:700; color:white; font-size:0.85em;">{contact['name']}</div>
                <div style="font-size:2em; font-weight:800; color:#f87171; letter-spacing:2px; margin:8px 0;">{contact['number']}</div>
                <div style="font-size:0.72em; color:rgba(255,255,255,0.4);">{contact['desc']}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    ec_cols2 = st.columns(3)
    for i, contact in enumerate(EMERGENCY_CONTACTS[4:]):
        with ec_cols2[i]:
            st.markdown(
                f"""
            <div style="background:rgba(220,38,38,0.08); border:1px solid rgba(220,38,38,0.2);
                border-radius:16px; padding:16px; text-align:center;">
                <div style="font-weight:600; color:white; font-size:0.85em;">{contact['name']}</div>
                <div style="font-size:1.6em; font-weight:800; color:#fca5a5; margin:6px 0;">{contact['number']}</div>
                <div style="font-size:0.72em; color:rgba(255,255,255,0.4);">{contact['desc']}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.divider()

    # Scam Detector
    st.markdown(
        '<div style="font-family:Poppins; font-size:1.3em; font-weight:700; color:white; margin-bottom:16px;">🔍 AI Scam Detector</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div style="color:rgba(255,255,255,0.5); margin-bottom:16px; font-size:0.9em;">Koi suspicious message mila? Yahaan paste karo — Sakhi AI check karegi 🤖</div>',
        unsafe_allow_html=True,
    )

    suspicious_msg = st.text_area(
        "Suspicious message paste karo",
        placeholder="Example: 'Congratulations! You've won 50 lakh rupees. Click here to claim...'",
        height=120,
        label_visibility="collapsed",
    )

    if st.button("🔍 Analyze for Scam", type="primary", use_container_width=False):
        if suspicious_msg.strip():
            with st.spinner("Analyzing message... 🔍"):
                result = analyze_scam(suspicious_msg)
            st.markdown(
                f"""
            <div style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1);
                border-radius:18px; padding:24px; margin-top:16px;">
                <div style="font-size:0.8em; color:rgba(255,255,255,0.4); margin-bottom:12px;">AI ANALYSIS RESULT</div>
                <div style="color:rgba(255,255,255,0.85); line-height:1.8; font-size:0.9em;">{result.replace(chr(10), '<br>')}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        else:
            st.warning("Pehle message paste karo!")

    st.divider()

    # Safety Resources
    st.markdown(
        '<div style="font-family:Poppins; font-size:1.3em; font-weight:700; color:white; margin-bottom:16px;">📚 Safety Resources</div>',
        unsafe_allow_html=True,
    )

    res_tabs = st.tabs(
        ["💻 Online Safety", "🚗 Travel Safety", "🏠 Home Safety", "⚠️ Common Scams"]
    )

    with res_tabs[0]:
        tips = [
            (
                "🔐",
                "Strong passwords",
                "Har account ke liye alag password use karo. Password manager try karo.",
            ),
            (
                "📱",
                "Two-factor auth",
                "2FA enable karo — yeh extra security layer deta hai.",
            ),
            (
                "🕵️",
                "Privacy settings",
                "Social media pe location aur personal info share mat karo.",
            ),
            (
                "🎣",
                "Phishing emails",
                "Unknown links pe click mat karo. Sender verify karo.",
            ),
            (
                "📸",
                "Photo safety",
                "Intimate photos share mat karo. Kisi ke saath bhi nahi.",
            ),
            (
                "💬",
                "Online harassment",
                "Harasser ko block+report karo. Evidence save karo.",
            ),
        ]
        cols = st.columns(3)
        for i, (icon, title, desc) in enumerate(tips):
            with cols[i % 3]:
                st.markdown(
                    f"""
                <div style="background:rgba(255,255,255,0.04); border-radius:14px; padding:16px; margin-bottom:12px;">
                    <div style="font-size:1.5em; margin-bottom:6px;">{icon}</div>
                    <div style="font-weight:600; color:white; font-size:0.88em; margin-bottom:4px;">{title}</div>
                    <div style="font-size:0.78em; color:rgba(255,255,255,0.5);">{desc}</div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

    with res_tabs[1]:
        st.markdown(
            """
        <div style="color:rgba(255,255,255,0.8); line-height:2; font-size:0.9em;">
        🚕 <strong>Cab Safety:</strong> Trip share karo family ke saath. OLA/UBER mein emergency button use karo.<br>
        📍 <strong>Location sharing:</strong> Trusted contacts ke saath live location share karo.<br>
        🌙 <strong>Night travel:</strong> Alone raat ko travel avoid karo. Trusted company rakho.<br>
        📞 <strong>Check-ins:</strong> Destination pe pahunche toh family ko inform karo.<br>
        👥 <strong>Public transport:</strong> Well-lit aur crowded areas prefer karo.<br>
        🏨 <strong>Hotels:</strong> Sirf registered hotels mein ruko. Room number share mat karo strangers ke saath.
        </div>
        """,
            unsafe_allow_html=True,
        )

    with res_tabs[2]:
        st.markdown(
            """
        <div style="color:rgba(255,255,255,0.8); line-height:2; font-size:0.9em;">
        🔒 <strong>Doors & windows:</strong> Raat ko sab lock karo. CCTV consider karo.<br>
        📣 <strong>Trusted neighbors:</strong> Emergency contact ke taur pe neighbors ko inform karo.<br>
        🏃 <strong>Escape plan:</strong> Fire ya emergency mein nikaas ka rasta pata hona chahiye.<br>
        📱 <strong>Emergency contacts:</strong> Speed dial pe Police 100 aur family rakho.<br>
        🔑 <strong>Spare keys:</strong> Sirf trusted logon ko do. Locks change karo agar zarurat ho.
        </div>
        """,
            unsafe_allow_html=True,
        )

    with res_tabs[3]:
        scams = [
            (
                "📞 KYC Scam",
                "Bank/UIDAI se call aata hai KYC update ke liye. Kabhi OTP share mat karo!",
            ),
            (
                "💰 Lottery Scam",
                "'Aapne 50 lakh jeeta' — yeh hamesha scam hai. Paise dene ki zarurat nahi.",
            ),
            (
                "💼 Job Scam",
                "Advance fee maangne wali job offers fake hain. Legit companies payment nahi maangti.",
            ),
            (
                "❤️ Romance Scam",
                "Online stranger jo jaldi paise maange — scammer hai. Feelings exploit karte hain.",
            ),
            (
                "🏦 UPI Scam",
                "Money 'receive' karne ke liye UPI pin daalna zaruri nahi. Yeh fraud hai.",
            ),
            (
                "👮 Police Scam",
                "Fake cops jo phone pe dhamkate hain aur paise maangte hain — 100 pe verify karo.",
            ),
        ]
        scam_cols = st.columns(2)
        for i, (name, desc) in enumerate(scams):
            with scam_cols[i % 2]:
                st.markdown(
                    f"""
                <div style="background:rgba(245,158,11,0.08); border:1px solid rgba(245,158,11,0.2);
                    border-radius:14px; padding:16px; margin-bottom:10px;">
                    <div style="font-weight:700; color:#fbbf24; font-size:0.88em; margin-bottom:6px;">{name}</div>
                    <div style="font-size:0.8em; color:rgba(255,255,255,0.6);">{desc}</div>
                </div>
                """,
                    unsafe_allow_html=True,
                )
