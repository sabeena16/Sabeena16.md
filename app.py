from flask import Flask, render_template, request
import pdfplumber

app = Flask(__name__)

SKILLS = [
    "Python", "Java", "C", "C++", "JavaScript",
    "HTML", "CSS", "SQL", "Machine Learning",
    "Data Science", "Flask", "Django",
    "React", "Git", "AI"
]

def extract_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return text

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']

    if not file:
        return "Please upload a resume."

    text = extract_text(file)

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    score = int((len(found_skills) / len(SKILLS)) * 100)

    recommendations = [s for s in SKILLS if s not in found_skills]

    return render_template(
        "result.html",
        skills=found_skills,
        score=score,
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)
