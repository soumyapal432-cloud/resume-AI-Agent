def get_prompt(resume, job_description, ats_score, missing_skills):

    prompt = f"""
You are a Resume Career AI Assistant.

Resume:
{resume}

Job Description:
{job_description}

ATS Score:
{ats_score}

Missing Skills:
{missing_skills}

Please give the output in this format only.

ATS Score:

Resume Skills:

Missing Skills:

Resume Improvement:

Resume Summary:

Cover Letter:
"""

    return prompt