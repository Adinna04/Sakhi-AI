import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile"
APP_NAME = "Sakhi AI"
APP_TAGLINE = "Har Ladki Ki Digital Saheli 💙"

PAGES = {
    "🏠 Home": "home",
    "💬 Sakhi Chat": "chat",
    "🏥 Health": "health",
    "🛡️ Safety": "safety",
    "👤 Profile": "profile",
}

CHAT_MODES = {
    "💜 General Sakhi": {
        "icon": "💜",
        "prompt": """Tu Sakhi hai — ek caring, empathetic AI saheli for Indian girls and women.
Tu Hinglish mein baat karti hai (Hindi + English mix).
Tu helpful, warm, non-judgmental hai. Emojis use kar naturally.
Topics: health, career, relationships, education, safety, government schemes, legal rights.
Agar koi distress mein ho toh helpline numbers de: Women Helpline 1091, iCall 9152987821.""",
    },
    "🩺 Health Expert": {
        "icon": "🩺",
        "prompt": """Tu ek women's health expert AI hai.
PCOS, periods, menstrual health, mental health, nutrition ke baare mein expert guidance de.
Always recommend consulting a real doctor for serious issues.
Hinglish mein baat kar, caring aur informative ho.""",
    },
    "🎓 Career Mentor": {
        "icon": "🎓",
        "prompt": """Tu ek career mentor AI hai for Indian women and girls.
Career guidance, skill development, internships, job search, interview prep pe help kar.
Current Indian job market ke baare mein practical advice de.
Hinglish mein baat kar, motivating aur actionable ho.""",
    },
    "⚖️ Legal Guide": {
        "icon": "⚖️",
        "prompt": """Tu ek women's legal rights guide AI hai for India.
Indian laws related to women: workplace rights, domestic violence, property rights, marriage laws ke baare mein batao.
Always note: yeh general information hai, legal advice ke liye advocate se milo.
Hinglish mein baat kar, clear aur helpful ho.""",
    },
    "🛡️ Safety Advisor": {
        "icon": "🛡️",
        "prompt": """Tu ek personal safety advisor AI hai for Indian women.
Online safety, travel safety, personal safety tips, emergency procedures ke baare mein batao.
Emergency mein helpline numbers do: Police 100, Women Helpline 1091, Ambulance 108.
Hinglish mein baat kar, practical aur empowering ho.""",
    },
}

MOOD_OPTIONS = [
    "😊 Khush",
    "😍 Excited",
    "😰 Anxious",
    "😔 Udaas",
    "😴 Tired",
    "💪 Motivated",
    "😤 Frustrated",
    "🤒 Unwell",
]

EMERGENCY_CONTACTS = [
    {"name": "Women Helpline", "number": "1091", "desc": "24/7 Available"},
    {"name": "Police", "number": "100", "desc": "Emergency"},
    {"name": "Ambulance", "number": "108", "desc": "Medical Emergency"},
    {"name": "Domestic Violence", "number": "181", "desc": "NCW Helpline"},
    {
        "name": "iCall Mental Health",
        "number": "9152987821",
        "desc": "Mon–Sat, 8am–10pm",
    },
    {"name": "Childline", "number": "1098", "desc": "Under 18"},
    {"name": "Cyber Crime", "number": "1930", "desc": "Online Safety"},
]

SCHOLARSHIPS = [
    {
        "name": "AICTE Pragati Scholarship",
        "amount": "₹50,000/year",
        "for": "Technical education girls",
        "state": "All India",
        "course": "Engineering/Technology",
        "income": "Below 8 LPA",
        "link": "https://scholarships.gov.in",
    },
    {
        "name": "Begum Hazrat Mahal Scholarship",
        "amount": "₹5,000–₹6,000",
        "for": "Minority girls class 9-12",
        "state": "All India",
        "course": "School",
        "income": "Below 2 LPA",
        "link": "https://scholarships.gov.in",
    },
    {
        "name": "Indira Gandhi Scholarship",
        "amount": "₹3,100/month",
        "for": "Single girl child PG",
        "state": "All India",
        "course": "Postgraduate",
        "income": "Any",
        "link": "https://scholarships.gov.in",
    },
    {
        "name": "Sukanya Samriddhi Yojana",
        "amount": "8.2% interest",
        "for": "Girls below 10 years",
        "state": "All India",
        "course": "Any",
        "income": "Any",
        "link": "https://www.nsiindia.gov.in",
    },
    {
        "name": "Medhavi Chhatra Puraskar",
        "amount": "₹25,000",
        "for": "Meritorious girl students",
        "state": "All India",
        "course": "Any",
        "income": "Below 3.5 LPA",
        "link": "https://scholarships.gov.in",
    },
    {
        "name": "West Bengal Kanyashree",
        "amount": "₹25,000",
        "for": "WB girls 13-18 years",
        "state": "West Bengal",
        "course": "School",
        "income": "Below 1.2 LPA",
        "link": "https://wbkanyashree.gov.in",
    },
    {
        "name": "Maharashtra Minority Scholarship",
        "amount": "₹5,000–₹8,000",
        "for": "Minority girls",
        "state": "Maharashtra",
        "course": "School/College",
        "income": "Below 2 LPA",
        "link": "https://mahadbt.maharashtra.gov.in",
    },
    {
        "name": "Rajasthan Gargi Puraskar",
        "amount": "₹5,000",
        "for": "Girls scoring 75%+ in 10th",
        "state": "Rajasthan",
        "course": "School",
        "income": "Any",
        "link": "https://rajasthan.gov.in",
    },
    {
        "name": "Delhi Merit Scholarship",
        "amount": "₹1,000–₹2,500/month",
        "for": "Delhi girl students",
        "state": "Delhi",
        "course": "School/College",
        "income": "Below 2.5 LPA",
        "link": "https://edudel.nic.in",
    },
    {
        "name": "Tata Trust Scholarship",
        "amount": "Up to ₹1,50,000",
        "for": "Undergraduate girls",
        "state": "All India",
        "course": "Undergraduate",
        "income": "Below 4 LPA",
        "link": "https://tatatrusts.org",
    },
]

DAILY_QUOTES = [
    "She believed she could, so she did. 🌸",
    "A girl with a dream is unstoppable. 💫",
    "Your only limit is your mind. Break it. 💪",
    "Be the girl who decided to go for it. 🚀",
    "Strong women don't have attitudes, they have standards. 👑",
    "Educate a girl, empower a nation. 📚",
    "You are braver than you believe. 🦋",
    "The future belongs to those who believe in their dreams. ✨",
    "Apni awaaz buland karo — duniya sunegi. 🌺",
    "Khud pe yakeen rakho — sapne zarur poore honge. 💙",
]

GOVERNMENT_SCHEMES = [
    {
        "name": "Beti Bachao Beti Padhao",
        "desc": "Girl child welfare & education",
        "ministry": "WCD Ministry",
    },
    {
        "name": "PM Ujjwala Yojana",
        "desc": "Free LPG connection for BPL women",
        "ministry": "Petroleum Ministry",
    },
    {
        "name": "Mahila Shakti Kendra",
        "desc": "Community support for rural women",
        "ministry": "WCD Ministry",
    },
    {
        "name": "One Stop Centre",
        "desc": "Support for violence-affected women",
        "ministry": "WCD Ministry",
    },
    {
        "name": "Pradhan Mantri Matru Vandana",
        "desc": "₹5,000 for first pregnancy",
        "ministry": "WCD Ministry",
    },
    {
        "name": "Swadhar Greh",
        "desc": "Shelter for women in difficult circumstances",
        "ministry": "WCD Ministry",
    },
]
