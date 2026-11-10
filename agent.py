
import os
from groq import Groq
from dotenv import load_dotenv

from tools import (
    extract_skills,
    recommend_jobs,
    analyze_skill_gap
)

# Load API key
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def career_agent(user_skills):

    print("AI Career Agent Started!")

    # Step 1: Extract skills
    skills = extract_skills(user_skills)

    # Step 2: Recommend jobs
    recommendations = recommend_jobs(skills)

    # Step 3: Analyze skill gaps
    gaps = analyze_skill_gap(skills)

    # Step 4: Generate AI career advice
    prompt = f"""
    You are an expert career guidance assistant.

    Candidate Skills: {skills}

    Job Recommendations: {recommendations}

    Skill Gaps: {gaps}

    Provide:
    1. Career guidance.
    2. Important skills to learn.
    3. A practical 30-day learning roadmap.
    4. Suitable career opportunities for a fresher.

    Keep the explanation simple and practical.
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    career_advice = response.choices[0].message.content

    return recommendations, gaps, career_advice
