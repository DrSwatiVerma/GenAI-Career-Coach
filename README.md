# 🎓 GenAI Career & College Coach

An AI-powered career assistant that helps students and early professionals with:
1. **Resume Optimization** – Add role-specific keywords to make resumes ATS-friendly.
2. **Interview Simulator** – Generate tailored interview Q&A for different job roles.
3. **Global College Finder** – Suggest universities worldwide based on specialization.

---

## 🚀 Features
- Upload/Paste Resume → Get an optimized version.
- Enter Job Role → Get 3–5 interview questions with sample answers.
- Search by Specialization → Get a list of global universities from a sample dataset.

---

## 🏗 Project Structure
```
GenAI-Career-Coach/
│
├── app.py # Main Streamlit app
├── requirements.txt # Dependencies
├── data/
│ └── colleges.json # Sample college/university dataset
├── utils/
│ ├── resume_helper.py # Resume optimization functions
│ ├── interview_helper.py # Interview Q&A generator
│ └── college_helper.py # College recommendation engine
└── README.md # Project documentation
'''

---
'''
## 🔧 Installation & Running
1. Clone this repository:
   ```bash
   git clone https://github.com/DrSwatiVerma/GenAI-Career-Coach
   cd GenAI-Career-Coach

2. Create a virtual environment:

python -m venv venv
source venv/bin/activate    # Mac/Linux
.\venv\Scripts\activate     # Windows

3. Install dependencies:

pip install -r requirements.txt


4. Run the app:

streamlit run app.py


5. Open your browser at http://localhost:8501.
'''