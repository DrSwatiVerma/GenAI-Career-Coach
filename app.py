import streamlit as st
from utils.resume_helper import optimize_resume
from utils.interview_helper import generate_interview_qna
from utils.college_helper import recommend_colleges

st.set_page_config(page_title="GenAI Career Coach", layout="wide")

st.title("🎓 GenAI Career & College Coach")

menu = st.sidebar.radio("Choose Feature", ["Resume Optimizer", "Interview Q&A", "College Finder"])

if menu == "Resume Optimizer":
    st.header("📄 Resume Optimizer")
    job_role = st.text_input("Enter Job Role (e.g., Data Scientist, Software Engineer)")
    resume_text = st.text_area("Paste Your Resume")
    if st.button("Optimize"):
        result = optimize_resume(resume_text, job_role)
        st.subheader("Optimized Resume:")
        st.write(result)

elif menu == "Interview Q&A":
    st.header("🎤 Interview Simulator")
    job_role = st.text_input("Enter Job Role")
    if st.button("Generate Q&A"):
        qna = generate_interview_qna(job_role)
        for item in qna:
            st.write("**Q:**", item["question"])
            st.write("**A:**", item["answer"])

elif menu == "College Finder":
    st.header("🏫 Global College Finder")
    specialization = st.text_input("Enter Specialization (e.g., AI, Finance, Engineering)")
    if st.button("Find Colleges"):
        results = recommend_colleges(specialization)
        if results:
            for r in results:
                st.write(f"**{r['name']}** - {r['country']} (Tuition: {r['tuition']})")
        else:
            st.write("No matching colleges found.")
