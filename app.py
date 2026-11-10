
import streamlit as st

from agent import career_agent

st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Career Assistant")

st.write("Find suitable career opportunities using AI")

name = st.text_input("Enter your name")

skills = st.text_input(
    "Enter your technical skills (comma separated)"
)

experience = st.selectbox(
    "Select your experience",
    ["Fresher", "0-1 Years", "1-3 Years", "3+ Years"]
)

if st.button("Analyze My Profile"):

    if name.strip() and skills.strip():

        st.success("Profile submitted successfully!")

        st.subheader("Candidate Profile")

        st.write("**Name:**", name)
        st.write("**Skills:**", skills)
        st.write("**Experience:**", experience)

        with st.spinner("AI is analyzing your career..."):

            recommendations, gaps, career_advice = career_agent(skills)

        st.subheader("Recommended Job Roles")

        for item in recommendations:

            st.write("###", item["role"])

            st.progress(item["match_score"] / 100)

            st.write(
                "**Match Score:**",
                str(item["match_score"]) + "%"
            )

            st.write(
                "**Matched Skills:**",
                ", ".join(item["matched_skills"]) or "None"
            )

            st.write(
                "**Missing Skills:**",
                ", ".join(item["missing_skills"]) or "None"
            )

            st.divider()

        st.subheader("Skill Gap Analysis")

        for job, missing in gaps.items():

            st.write(
                "**" + job + ":**",
                ", ".join(missing) or "No missing skills"
            )

        st.subheader("🤖 AI Generated Career Roadmap")

        st.markdown(career_advice)

    else:

        st.warning("Please enter your name and technical skills.")
