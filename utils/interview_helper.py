def generate_interview_qna(job_role):
    """
    Simulate interview questions for a role.
    """
    questions = {
        "Data Scientist": [
            "Explain the bias-variance tradeoff.",
            "How would you handle missing data in a dataset?"
        ],
        "Software Engineer": [
            "What are REST APIs?",
            "How do you ensure code scalability?"
        ],
        "AI Researcher": [
            "What is the difference between supervised and unsupervised learning?",
            "How do transformers work?"
        ]
    }

    qna = []
    for q in questions.get(job_role, ["Tell me about yourself."]):
        qna.append({"question": q, "answer": "Sample answer for: " + q})

    return qna
