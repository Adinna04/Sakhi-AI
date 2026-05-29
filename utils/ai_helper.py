from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)


def get_ai_response(
    messages: list, system_prompt: str, temperature: float = 0.7
) -> str:
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "system", "content": system_prompt}] + messages,
            temperature=temperature,
            max_tokens=1024,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Oops! Technical issue aa gaya 🌸 Error: {str(e)}\n\nThodi der baad try karo!"


def analyze_scam(text: str) -> str:
    prompt = """You are a scam detection expert for India.
Analyze the following message and determine if it's a scam or safe.
Respond in Hinglish with:
1. VERDICT: 🚨 LIKELY SCAM / ⚠️ SUSPICIOUS / ✅ LIKELY SAFE
2. REASONS: 3 bullet points explaining why
3. ADVICE: What should the person do
Be clear and practical."""
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": f"Analyze this message for scam:\n\n{text}"}
            ],
            system=prompt,
            temperature=0.3,
            max_tokens=512,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Analysis failed: {str(e)}"


def get_career_roadmap(course: str, year: str, goal: str) -> str:
    prompt = f"""Create a detailed career roadmap for an Indian girl:
Course: {course}
Year: {year}
Career Goal: {goal}

Provide in Hinglish:
1. 🎯 Top 5 skills to develop
2. 💼 3-5 relevant internships/projects
3. 📚 Learning resources (free & paid)
4. 🗓️ 6-month action plan
5. 💰 Expected salary range in India
6. 🌐 Top companies to target

Be specific, practical, and encouraging!"""
    return get_ai_response(
        [{"role": "user", "content": prompt}],
        "You are a career mentor for Indian women.",
        0.5,
    )
