import spacy
import PyPDF2
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "python", "java", "c", "machine learning", "deep learning",
    "nlp", "sql", "flask", "django", "data analysis",
    "tensorflow", "keras", "opencv"
]

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def preprocess(text):
    doc = nlp(text.lower())
    tokens = [t.lemma_ for t in doc if t.is_alpha and not t.is_stop]
    return " ".join(tokens)

def extract_skills(text):
    found = set()
    for skill in SKILLS_DB:
        if skill in text:
            found.add(skill)
    return list(found)

def rank_resumes(job_desc, resumes, resumes_skills):
    corpus = [job_desc] + resumes
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(corpus)

    similarity_scores = cosine_similarity(tfidf[0:1], tfidf[1:])[0]

    final_scores = []

    job_skills = extract_skills(job_desc)

    for i, base_score in enumerate(similarity_scores):
        matched_skills = set(job_skills) & set(resumes_skills[i])

        # Skill boost logic
        skill_bonus = len(matched_skills) * 0.05  # each skill adds 5%

        final_score = min(base_score + skill_bonus, 1.0)
        final_scores.append(final_score)

    return final_scores

