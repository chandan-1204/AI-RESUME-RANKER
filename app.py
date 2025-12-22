from flask import Flask, render_template, request, send_file
import os, csv
from utils import extract_text_from_pdf, preprocess, rank_resumes, extract_skills

app = Flask(__name__)
UPLOAD_FOLDER = "resumes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    ranked = []
    if request.method == "POST":
        job_desc = preprocess(request.form["job_desc"])
        files = request.files.getlist("resumes")

        resume_data = []

        for file in files:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)
            text = extract_text_from_pdf(path)
            clean = preprocess(text)
            skills = extract_skills(clean)
            resume_data.append((file.filename, clean, skills))

        scores = rank_resumes(
    job_desc,
    [r[1] for r in resume_data],
    [r[2] for r in resume_data]
)


        ranked = sorted(
            [(resume_data[i][0], scores[i], resume_data[i][2]) for i in range(len(scores))],
            key=lambda x: x[1],
            reverse=True
        )

        # Save CSV
        with open("ranking_report.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Resume", "Score", "Skills"])
            for r in ranked:
                writer.writerow([r[0], round(r[1], 2), ", ".join(r[2])])

    return render_template("index.html", ranked=ranked)

@app.route("/download")
def download():
    return send_file("ranking_report.csv", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
