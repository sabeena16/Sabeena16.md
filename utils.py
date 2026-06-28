def calculate_score(found_skills, total_skills):
    if total_skills == 0:
        return 0
    return int((len(found_skills) / total_skills) * 100)
