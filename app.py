import streamlit as st

st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="💼",
    layout="wide"
)

st.title(" AI Career Assistant")
st.write("Generate Resume Summaries, Cover Letters, Interview Questions, and Skill Suggestions.")

st.sidebar.header("Choose a Feature")

feature = st.sidebar.selectbox(
    "Select Feature",
    [
        "Resume Summary Generator",
        "Cover Letter Generator",
        "Interview Questions Generator",
        "Skill Suggestions"
    ]
)

st.subheader(feature)

name = st.text_input("Your Name")
job_role = st.text_input("Target Job Role")
experience = st.number_input(
    "Years of Experience",
    min_value=0,
    max_value=50,
    value=1
)

skills = st.text_area(
    "Enter Skills (comma separated)",
    placeholder="Python, SQL, Streamlit, GitHub"
)

skill_list = [s.strip() for s in skills.split(",") if s.strip()]

if st.button("Generate"):

    if not name or not job_role or not skills:
        st.warning("Please fill all fields.")
        st.stop()

    # Resume Summary Generator
    if feature == "Resume Summary Generator":

        summary = f"""
{name} is a motivated {job_role} with {experience} years of experience.
Skilled in {", ".join(skill_list)}.

Demonstrates strong problem-solving abilities, adaptability, and a commitment
to continuous learning. Passionate about delivering high-quality work and
contributing effectively to team success.
"""

        st.success("Resume Summary Generated")
        st.text_area("Output", summary, height=220)

    # Cover Letter Generator
    elif feature == "Cover Letter Generator":

        letter = f"""
Dear Hiring Manager,

I am writing to express my interest in the {job_role} position.

With {experience} years of experience and skills in
{", ".join(skill_list)}, I have developed a strong foundation in
technical and professional problem-solving.

I am enthusiastic about contributing my knowledge, learning new
technologies, and helping organizations achieve their goals.

I would welcome the opportunity to discuss how my background and
skills can benefit your team.

Thank you for your time and consideration.

Sincerely,

{name}
"""

        st.success("Cover Letter Generated")
        st.text_area("Output", letter, height=350)

    # Interview Questions Generator
    elif feature == "Interview Questions Generator":

        questions = [
            f"Tell us about your experience as a {job_role}.",
            f"How have you used {skill_list[0]} in your projects?",
            "Describe a challenging problem you solved.",
            "How do you handle tight deadlines?",
            "What are your strengths and weaknesses?",
            "How do you keep your skills updated?",
            "Explain a project you are proud of.",
            "How do you work in a team environment?",
            "Why should we hire you?",
            "Where do you see yourself in five years?"
        ]

        st.success("Interview Questions Generated")

        for i, q in enumerate(questions, start=1):
            st.write(f"{i}. {q}")

    # Skill Suggestions
    elif feature == "Skill Suggestions":

        suggestions = []

        if "python" not in skills.lower():
            suggestions.append("Python")

        if "sql" not in skills.lower():
            suggestions.append("SQL")

        if "github" not in skills.lower():
            suggestions.append("Git & GitHub")

        if "api" not in skills.lower():
            suggestions.append("REST APIs")

        if "streamlit" not in skills.lower():
            suggestions.append("Streamlit")

        if "cloud" not in skills.lower():
            suggestions.append("Cloud Deployment")

        if "communication" not in skills.lower():
            suggestions.append("Communication Skills")

        st.success("Recommended Skills")

        if suggestions:
            for skill in suggestions:
                st.write("✅", skill)
        else:
            st.write("Great! Your skill set already looks strong.")

st.markdown("---")
st.caption("AI Career Assistant | Assignment 39")