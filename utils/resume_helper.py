def optimize_resume(resume_text, job_role):
    """
    Simple function to optimize resume by adding role-specific keywords.
    For hackathon, we simulate with a predefined dictionary.
    """
    keywords = {
        "Data Scientist": ["Python", "Machine Learning", "Statistics", "SQL"],
        "Software Engineer": ["Java", "APIs", "Cloud", "Agile"],
        "AI Researcher": ["Deep Learning", "LLMs", "Neural Networks", "TensorFlow"]
    }

    job_keywords = keywords.get(job_role, [])
    optimized_resume = resume_text + "\n\n[Optimized for role: " + job_role + "]\n"
    optimized_resume += "Keywords added: " + ", ".join(job_keywords)

    return optimized_resume
