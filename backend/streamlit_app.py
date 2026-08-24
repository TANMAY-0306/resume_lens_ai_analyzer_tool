import os
import streamlit as st

from app.readers import read_resume
from app.resume_parser import parse_resume
from app.job_parser import parse_job_description
from app.matcher import calculate_match_score


st.set_page_config(
    page_title="ResumeMatch AI",
    page_icon="📄",
    layout="wide"
)

st.title("📄 ResumeMatch AI")
st.caption("AI-Powered Resume Screening & Job Matching")

st.markdown("---")

with st.sidebar:
    st.header("About")

    st.write(
        """
        Upload a resume and compare it against a job description.
        
        The AI will:
        - Extract resume information
        - Parse job requirements
        - Calculate a match score
        - Identify missing skills
        - Provide improvement suggestions
        """
    )

    st.markdown("---")

    st.write("Built with:")
    st.write("• Python")
    st.write("• Streamlit")
    st.write("• Groq")
    st.write("• Pydantic")


resume_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250,
    placeholder="Paste the job description here..."
)

analyze_button = st.button(
    "Analyze Resume",
    use_container_width=True
)

if analyze_button:

    if resume_file is None:
        st.error("Please upload a resume.")
        st.stop()

    if not job_description.strip():
        st.error("Please provide a job description.")
        st.stop()

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        resume_file.name
    )

    with open(file_path, "wb") as f:
        f.write(resume_file.getbuffer())

    with st.spinner("Analyzing Resume..."):

        resume_text = read_resume(file_path)

        resume = parse_resume(resume_text)

        job = parse_job_description(job_description)

        result = calculate_match_score(
            job,
            resume
        )

    st.success("Analysis Complete")

    st.metric(
        "Job Match Score",
        f"{result.job_match_score}%"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Matching Skills")

        for skill in result.details.matching_skills:
            st.write(f"• {skill}")

    with col2:
        st.subheader("❌ Missing Skills")

        for skill in result.details.missing_skills:
            st.write(f"• {skill}")

    st.subheader("💪 Strengths")

    for strength in result.details.strengths:
        st.write(f"• {strength}")

    st.subheader("📈 Suggestions")

    for suggestion in result.details.suggestions:
        st.write(f"• {suggestion}")

    st.subheader("🎯 Final Verdict")

    st.info(result.details.verdict)