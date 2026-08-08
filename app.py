import streamlit as st

from agent import ask_ai
from tools import (
    extract_resume_text,
    extract_skills,
    compare_skills,
    calculate_ats
)
from prompt import get_prompt

st.set_page_config(
    page_title="Resume & Career AI Agent",
    page_icon="📄"
)

st.title("📄 Resume & Career AI Agent")
st.write("Upload your Resume and paste the Job Description.")

# Upload Resume
resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# Job Description
job_description = st.text_area(
    "Paste Job Description",
    height=200
)

# Analyze Button
if st.button("Analyze Resume"):

    if resume_file is None:
        st.warning("Please upload your Resume.")
        st.stop()

    if job_description.strip() == "":
        st.warning("Please paste the Job Description.")
        st.stop()

    # Resume Text
    resume_text = extract_resume_text(resume_file)

    # Resume Skills
    resume_skills = extract_skills(resume_text)

    # Compare Skills
    matched, missing = compare_skills(
        resume_skills,
        job_description
    )

    # ATS Score
    ats_score = calculate_ats(
        matched,
        len(matched) + len(missing)
    )

    # Create Prompt
    prompt = get_prompt(
        resume_text,
        job_description,
        ats_score,
        missing
    )

    with st.spinner("Analyzing Resume..."):
        result = ask_ai(prompt)

    st.success("Analysis Completed!")

    st.subheader("ATS Score")
    st.success(f"{ats_score}%")

    st.subheader("Resume Skills")
    st.write(resume_skills)

    st.subheader("Missing Skills")
    st.write(missing)

    st.subheader("AI Analysis")
    st.write(result)