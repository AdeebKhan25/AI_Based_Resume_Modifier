# AI-Based Resume Modifier

An LLM-powered CLI tool that customizes a LaTeX resume (`.tex`) for a specific job description by aligning content, skills, and phrasing to the role requirements.

The tool takes:

- an existing LaTeX resume
- a job description
- optional new skills from the user

and generates a **modified resume** optimized for the given job.

## Why this project exists

Manually tailoring resumes for each job is:

- repetitive
- error-prone
- time-consuming

This project automates the process using an LLM (Google Gemini) while preserving the original LaTeX structure and formatting.

## Features

- Parses resume content from a `.tex` file
- Extracts and analyzes job requirements from a `.txt` job description
- Accepts additional skills interactively
- Uses an LLM to:
  - align resume content with job requirements
  - enhance skill relevance
  - keep formatting intact
- Outputs a modified LaTeX resume ready for compilation

## Project Structure
```bash
AI-Based_Resume_Modifier/
├── main.py                     # CLI entry point
├── llm.py                      # Gemini LLM interface and prompt logic
├── job_descrp.txt              # Sample job description (generated / intermediate)
├── .env.example                # Environment variable template
├── .gitignore
└── README.md
```

## Getting Started

To get started with this project locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/AdeebKhan25/AI_Based_Resume_Modifier.git
cd AI_Based_Resume_Modifier
```

2. Create a virtual enviroment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run command for usage:

```bash
python main.py {resume tex file} {job description txt file}
# example : python main.py resume.tex job_description.txt
```

You will be prompted to enter additional skills interactively - (optional, leave it empty if not required)

```bash
Enter the new skills -
```

5. Check the generated output:

```bash
modified_<resume_name>.tex → tailored resume
content.txt → extracted resume content
job_descrp.txt → processed job description
new_skills.txt → processed skill input
```

### Disclaimer

This tool assists with resume tailoring but does not guarantee interview calls.

### Further Assistance

If you need any more help or have other questions, feel free to ask. Happy coding! 🚀
