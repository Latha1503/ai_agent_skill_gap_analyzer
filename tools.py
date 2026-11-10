
# Available job roles and their required skills

job_roles = {
    "Java Developer": [
        "java", "sql", "oops", "coding",
        "data structures", "spring boot", "git"
    ],

    "Frontend Developer": [
        "html", "css", "javascript", "react"
    ],

    "Full Stack Developer": [
        "html", "css", "javascript",
        "react", "node.js", "sql"
    ],

    "Python Developer": [
        "python", "sql", "oops", "coding",
        "data structures", "git"
    ],

    "Machine Learning Engineer": [
        "python", "machine learning",
        "deep learning", "sql", "numpy",
        "pandas", "scikit-learn"
    ],

    "AI Engineer": [
        "python", "machine learning",
        "deep learning", "generative ai",
        "llm", "sql"
    ],

    "Data Scientist": [
        "python", "sql", "machine learning",
        "statistics", "pandas", "numpy"
    ],

    "Data Analyst": [
        "python", "sql", "excel",
        "power bi", "statistics"
    ]
}


# Step 1: Extract and clean skills

def extract_skills(user_skills):

    if isinstance(user_skills, str):
        skills = user_skills.lower().split(",")

    else:
        skills = [skill.lower() for skill in user_skills]

    skills = [skill.strip() for skill in skills if skill.strip()]

    return list(set(skills))


# Step 2: Recommend suitable job roles

def recommend_jobs(user_skills):

    skills = extract_skills(user_skills)

    recommendations = []

    for role, required_skills in job_roles.items():

        matched_skills = [
            skill for skill in required_skills
            if skill in skills
        ]

        missing_skills = [
            skill for skill in required_skills
            if skill not in skills
        ]

        match_score = round(
            (len(matched_skills) / len(required_skills)) * 100
        )

        recommendations.append({
            "role": role,
            "match_score": match_score,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills
        })

    # Highest match score first

    recommendations.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )

    return recommendations


# Step 3: Analyze skill gaps

def analyze_skill_gap(user_skills):

    recommendations = recommend_jobs(user_skills)

    skill_gaps = {}

    for job in recommendations:

        skill_gaps[job["role"]] = job["missing_skills"]

    return skill_gaps
