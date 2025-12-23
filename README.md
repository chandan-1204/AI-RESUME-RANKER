# 🚀 AI-Powered Resume Ranker

An AI-powered web application that automatically analyzes and ranks resumes based on their relevance to a given job description using Natural Language Processing (NLP) and Machine Learning techniques.

This project helps recruiters and HR teams shortlist candidates efficiently, reducing manual effort and bias.

---

## 📌 Features

- Upload multiple PDF resumes
- Paste job description
- NLP-based resume analysis
- Resume ranking using TF-IDF + Cosine Similarity
- Skill-weighted scoring for improved accuracy
- Visual score display with progress bars
- Extracted skill tags for each resume
- Download ranking report as CSV
- Responsive and modern UI with animations
- Light/Dark mode toggle

---

## 🛠 Technologies Used

### Backend
- Python
- Flask
- SpaCy
- Scikit-learn
- PyPDF2

### Frontend
- HTML
- CSS
- JavaScript

### ML / NLP Techniques
- Text preprocessing (lemmatization, stopword removal)
- TF-IDF Vectorization
- Cosine Similarity
- Skill-based score boosting

---

## 📁 Project Structure

resume_ranker/
│
├── app.py
├── utils.py
├── requirements.txt
├── resumes/
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
└── ranking_report.csv

---

## ⚙ Installation & Setup

### Step 1: Clone the Repository
https://github.com/chandan-1204/AI-RESUME-RANKER.git

### Step 2: Create Virtual Environment (Optional)
python -m venv venv
venv\Scripts\activate

### Step 3: Install Dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

---

## ▶ How to Run the Project

python app.py

Open your browser and go to:
http://127.0.0.1:5000

---

## 🧪 Sample Job Description (For Testing)

We are looking for an AI/ML Engineer with strong knowledge of Python,
Machine Learning, NLP, Deep Learning, Flask, and data analysis.

---

## 📊 How Ranking Works

1. Resume text is extracted from uploaded PDF files
2. Text is cleaned and preprocessed using NLP
3. TF-IDF converts text into numerical vectors
4. Cosine similarity measures relevance
5. Skill matching boosts final scores
6. Resumes are ranked from highest to lowest score

---

## 📈 Future Enhancements

- Use BERT or Sentence Transformers for better semantic similarity
- Add authentication for recruiters
- Deploy on cloud platforms (Render / Railway)
- Improve skill extraction using advanced NLP models
- Add resume-to-job skill comparison view

---

## 🎯 Use Cases

- HR resume screening
- Internship shortlisting
- Applicant Tracking System (ATS) prototype
- Academic and internship projects

---

## 🧠 Interview Explanation (One Line)

"I built an AI-based resume ranking system using NLP and machine learning that compares resumes with job descriptions and ranks candidates using similarity and skill-weighted scoring."

---

## 👨‍💻 Author

CHANDAN P R 
- B.E IN COMPUTER SCIENCE ENGINEERING (AI ML) 
- AI / ML Internship Project  

---

## 📜 License

This project is for educational and academic purposes only.

