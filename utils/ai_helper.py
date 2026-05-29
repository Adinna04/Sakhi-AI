from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = None

if GROQ_API_KEY:
    client = Groq(api_key=GROQ_API_KEY)


def get_ai_response(
    messages: list,
    system_prompt: str,
    temperature: float = 0.7,
) -> str:

    if not client:
        return (
            "⚠️ Groq API key not configured.\n\n"
            "Please add GROQ_API_KEY in Streamlit Secrets."
        )

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                }
            ]
            + messages,
            temperature=temperature,
            max_tokens=1024,
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Oops! Technical issue aa gaya 🌸\n\n" f"Error: {str(e)}"


def analyze_scam(text: str) -> str:

    if not client:
        return "⚠️ Groq API key not configured."

    prompt = """
You are a scam detection expert for India.

Analyze the following message and determine if it's a scam or safe.

Respond in Hinglish with:

1. VERDICT:
🚨 LIKELY SCAM
⚠️ SUSPICIOUS
✅ LIKELY SAFE

2. REASONS:
Give 3 bullet points

3. ADVICE:
What should the user do?
"""

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": prompt,
                },
                {
                    "role": "user",
                    "content": f"Analyze this message:\n\n{text}",
                },
            ],
            temperature=0.3,
            max_tokens=512,
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Analysis failed: {str(e)}"


def get_career_roadmap(
    course: str,
    year: str,
    goal: str,
) -> str:

    prompt = f"""
Create a detailed career roadmap for an Indian girl.

Course: {course}
Year: {year}
Career Goal: {goal}

Provide:

🎯 Top 5 skills to develop

💼 3-5 internships/projects

📚 Learning resources

🗓️ 6-month roadmap

💰 Salary expectations

🌐 Companies to target

Use Hinglish.
"""

    return get_ai_response(
        [{"role": "user", "content": prompt}],
        "You are a career mentor for Indian women.",
        0.5,
    )
