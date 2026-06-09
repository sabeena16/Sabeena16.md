# AI-Powered Resume Analyzer and Skill Recommendation System

## Project Title
AI-Powered Resume Analyzer and Skill Recommendation System

## Problem Statement
Many students and job seekers create resumes without knowing whether their skills match industry requirements. This project analyzes resumes automatically and provides recommendations for improvement.

## Project Objectives
1. To upload and analyze resumes in PDF format.
2. To extract candidate information and skills.
3. To compare extracted skills with industry requirements.
4. To generate a resume score.
5. To provide recommendations for improvement.
6. To improve employability and job readiness.

## Module List
1. User Registration and Login Module
2. Resume Upload Module
3. Resume Parsing Module
4. Skill Extraction Module
5. Resume Analysis and Scoring Module
6. Recommendation Module
7. Report Generation Module

## Table List

### User Table
- User_ID (Primary Key)
- Name
- Email
- Password

### Resume Table
- Resume_ID (Primary Key)
- User_ID (Foreign Key)
- File_Name
- Upload_Date

### Skills Table
- Skill_ID (Primary Key)
- Skill_Name

### Analysis_Report Table
- Report_ID (Primary Key)
- Resume_ID (Foreign Key)
- Resume_Score
- Recommendations

## Technologies Used

### Front End
- HTML
- CSS
- JavaScript
- Bootstrap

### Back End
- Python (Flask)

### Database
- MySQL

### Other Technologies
- Machine Learning
- Natural Language Processing (NLP)
- PyPDF2
- NLTK
- spaCy

## Expected Outcome
The system will analyze uploaded resumes, identify candidate skills, generate a resume score, and provide recommendations to improve resume quality and job readiness.
