from skill_matcher import SKILLS

def recommend_skills(found_skills):
    recommendations = []

    for skill in SKILLS:
        if skill not in found_skills:
            recommendations.append(skill)

    return recommendations
