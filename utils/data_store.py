import streamlit as st
from datetime import datetime

def init_session_state():
    defaults = {
        "messages": {},
        "current_page": "home",
        "mood_history": [],
        "current_mood": None,
        "period_data": {"last_date": None, "cycle_length": 28, "symptoms": []},
        "water_intake": 0,
        "journal_entries": [],
        "saved_chats": [],
        "bookmarks": [],
        "chat_mode": "💜 General Sakhi",
        "streak": 0,
        "last_visit": None,
        "achievements": [],
        "wellness_score": 0,
        "username": "Sakhi User",
        "language": "Hinglish",
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

    # Update streak
    today = datetime.now().date()
    if st.session_state.last_visit != today:
        if st.session_state.last_visit and (today - st.session_state.last_visit).days == 1:
            st.session_state.streak += 1
        elif st.session_state.last_visit is None:
            st.session_state.streak = 1
        st.session_state.last_visit = today

def add_mood(mood: str, note: str = ""):
    entry = {"mood": mood, "note": note, "date": datetime.now().strftime("%Y-%m-%d %H:%M")}
    st.session_state.mood_history.append(entry)
    st.session_state.current_mood = mood
    update_wellness_score()

def add_journal_entry(mood: str, note: str):
    entry = {"mood": mood, "note": note, "date": datetime.now().strftime("%Y-%m-%d %H:%M"), "id": len(st.session_state.journal_entries)}
    st.session_state.journal_entries.append(entry)

def update_wellness_score():
    score = 0
    if st.session_state.mood_history:
        score += min(len(st.session_state.mood_history) * 5, 30)
    if st.session_state.water_intake >= 8:
        score += 20
    if st.session_state.streak > 0:
        score += min(st.session_state.streak * 2, 20)
    if st.session_state.journal_entries:
        score += min(len(st.session_state.journal_entries) * 5, 30)
    st.session_state.wellness_score = min(score, 100)

def get_chat_messages(mode: str):
    if mode not in st.session_state.messages:
        st.session_state.messages[mode] = []
    return st.session_state.messages[mode]

def save_chat(mode: str):
    msgs = get_chat_messages(mode)
    if msgs:
        st.session_state.saved_chats.append({
            "mode": mode,
            "messages": msgs.copy(),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "id": len(st.session_state.saved_chats)
        })