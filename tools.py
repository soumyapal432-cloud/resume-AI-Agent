from pypdf import PdfReader

# Extract text from PDF
def extract_resume_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    return text


# Basic Skill List
SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "HTML",
    "CSS",
    "JavaScript",
    "SQL",
    "MySQL",
    "Git",
    "GitHub",
    "Docker",
    "AWS",
    "Excel",
    "Power BI",
    "Communication",
    "Leadership"
]


# Extract Skills
def extract_skills(text):
    found = []

    text = text.lower()

    for skill in SKILLS:
        if skill.lower() in text:
            found.append(skill)

    return found


# Compare Resume & JD Skills
def compare_skills(resume_skills, jd_text):

    jd_skills = extract_skills(jd_text)

    matched = []
    missing = []

    for skill in jd_skills:
        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    return matched, missing


# Calculate ATS Score
def calculate_ats(matched, total):

    if total == 0:
        return 0

    score = (len(matched) / total) * 100

    return round(score)