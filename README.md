# Resume & Career AI Agent

## Objective

This project analyzes a resume based on a Job Description using openrouter.

## Features

- Upload Resume (PDF)
- Enter Job Description
- Extract Resume Text
- Extract Skills
- Compare Resume with JD
- Calculate ATS Score
- Find Missing Skills
- Generate Resume Improvement Tips
- Generate Resume Summary
- Generate Cover Letter

## Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini API
- PyPDF

## Project Structure

Resume_AI_Agent/
│
├── app.py
├── agent.py
├── tools.py
├── prompt.py
├── requirements.txt
├── .env
└── README.md

## How to Run

1. Install Python
2. Install the required libraries

pip install -r requirements.txt

3. Add your Gemini API Key in .env

GOOGLE_API_KEY=your_api_key

4. Run the project

streamlit run app.py

## Output

- ATS Score
- Resume Skills
- Missing Skills
- Resume Improvement
- Resume Summary
- Cover Letter

## Author

Soumyajit Pal