import streamlit as st
from config import CHAT_MODES
from utils.data_store import get_chat_messages, save_chat
from utils.ai_helper import get_ai_response


def render_chat():
    st.markdown(
        '<div style="font-family:Poppins; font-size:1.8em; font-weight:800; color:white; margin-bottom:4px;">💬 Sakhi AI Chat</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div style="color:rgba(255,255,255,0.5); margin-bottom:24px;">Your safe space to talk about anything 💙</div>',
        unsafe_allow_html=True,
    )

    # Mode selector
    st.markdown(
        '<div style="font-size:0.85em; color:rgba(255,255,255,0.5); margin-bottom:10px; letter-spacing:1px;">SELECT CHAT MODE</div>',
        unsafe_allow_html=True,
    )
    mode_cols = st.columns(len(CHAT_MODES))
    for i, (mode_name, mode_data) in enumerate(CHAT_MODES.items()):
        with mode_cols[i]:
            is_active = st.session_state.chat_mode == mode_name
            if st.button(
                f"{mode_data['icon']} {mode_name.split(' ', 1)[1]}",
                key=f"mode_{i}",
                use_container_width=True,
                type="primary" if is_active else "secondary",
            ):
                st.session_state.chat_mode = mode_name
                st.rerun()

    current_mode = st.session_state.chat_mode
    st.markdown(
        f"""
    <div style="background:rgba(124,58,237,0.12); border:1px solid rgba(124,58,237,0.25);
        border-radius:14px; padding:12px 16px; margin:16px 0; display:flex; align-items:center; gap:10px;">
        <span style="font-size:1.4em;">{CHAT_MODES[current_mode]['icon']}</span>
        <div>
            <div style="color:white; font-weight:600; font-size:0.9em;">{current_mode}</div>
            <div style="color:rgba(255,255,255,0.4); font-size:0.78em;">Specialized AI mode active</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Action buttons
    col1, col2, col3 = st.columns([1, 1, 3])
    with col1:
        if st.button("🗑️ Clear Chat"):
            st.session_state.messages[current_mode] = []
            st.rerun()
    with col2:
        if st.button("🔖 Save Chat"):
            save_chat(current_mode)
            st.success("Chat saved!")

    st.divider()

    # Init messages
    messages = get_chat_messages(current_mode)
    if not messages:
        welcome_msgs = {
            "💜 General Sakhi": "Namaste! 🌸 Main Sakhi hoon — tumhari digital saheli! Kuch bhi poochho, main yahan hoon. 💙",
            "🩺 Health Expert": "Namaste! 🩺 Main tumhari health expert saheli hoon. Period health, PCOS, mental wellness — sab ke baare mein baat kar sakte hain!",
            "🎓 Career Mentor": "Hey! 🎓 Main tumhari career mentor hoon. Apne goals batao — milke ek roadmap banate hain!",
            "⚖️ Legal Guide": "Namaste! ⚖️ Main tumhare legal rights ke baare mein guide karungi. Koi bhi legal sawaal poochho!",
            "🛡️ Safety Advisor": "Hi! 🛡️ Main tumhari safety advisor hoon. Personal safety, online safety — sab discuss kar sakte hain.",
        }
        messages.append(
            {
                "role": "assistant",
                "content": welcome_msgs.get(
                    current_mode, "Namaste! Main Sakhi hoon 🌸"
                ),
            }
        )

    # Display messages
    for msg in messages:
        avatar = "🌸" if msg["role"] == "assistant" else "👤"
        with st.chat_message(msg["role"], avatar=avatar):
            st.write(msg["content"])

    # Quick prompts
    st.markdown(
        '<div style="font-size:0.8em; color:rgba(255,255,255,0.4); margin-bottom:8px;">QUICK PROMPTS</div>',
        unsafe_allow_html=True,
    )

    quick_prompts = {
        "💜 General Sakhi": [
            "Aaj mujhe kuch motivation chahiye",
            "Government schemes kya hain",
            "Self-care tips batao",
        ],
        "🩺 Health Expert": [
            "PCOS ke symptoms kya hain?",
            "Period pain ke gharelu upay",
            "Mental health improve kaise karein",
        ],
        "🎓 Career Mentor": [
            "Data science career kaise start karein?",
            "Interview tips chahiye",
            "Best free courses batao",
        ],
        "⚖️ Legal Guide": [
            "Workplace harassment pe kya rights hain?",
            "Property rights for women in India",
            "Domestic violence laws",
        ],
        "🛡️ Safety Advisor": [
            "Online safety tips chahiye",
            "Travel safety for solo girls",
            "Emergency mein kya karein",
        ],
    }

    prompts = quick_prompts.get(current_mode, [])
    if prompts:
        qp_cols = st.columns(len(prompts))
        for i, prompt in enumerate(prompts):
            with qp_cols[i]:
                if st.button(prompt, key=f"qp_{i}", use_container_width=True):
                    messages.append({"role": "user", "content": prompt})
                    with st.spinner("Sakhi soch rahi hai... 💭"):
                        reply = get_ai_response(
                            messages, CHAT_MODES[current_mode]["prompt"]
                        )
                    messages.append({"role": "assistant", "content": reply})
                    st.rerun()

    # Chat input
    if user_input := st.chat_input("Apna sawaal poochho... 💬"):
        messages.append({"role": "user", "content": user_input})
        with st.chat_message("user", avatar="👤"):
            st.write(user_input)
        with st.chat_message("assistant", avatar="🌸"):
            with st.spinner("Sakhi soch rahi hai... 💭"):
                reply = get_ai_response(messages, CHAT_MODES[current_mode]["prompt"])
            st.write(reply)
        messages.append({"role": "assistant", "content": reply})
        st.rerun()
