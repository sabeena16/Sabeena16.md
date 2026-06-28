SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "HTML",
    "CSS",
    "JavaScript",
    "SQL",
    "Flask",
    "Django",
    "React",
    "Machine Learning",
    "Data Science",
    "Artificial Intelligence",
    "Git",
    "AWS"
]

def find_skills(resume_text):
    found_skills = []

    for skill in SKILLS:
        if skill.lower() in resume_text.lower():
            found_skills.append(skill)

    return found_skills
