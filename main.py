import argparse
import os
from dotenv import load_dotenv
from pathlib import Path
from llm import GeminiLLM


# load the API KEY
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# read text directly
def read_file(tex_path):
    if tex_path.exists():
        tex_content = tex_path.read_text(encoding='utf-8')
        return tex_content
    else:
        print("Error: file doesn't exist!")

# save file
def save_file(tex_path, output_path="modified_resume.tex"):
    path = Path(output_path)
    path.write_text(tex_path, encoding='utf-8')
    print(f"Success: File saved to {path}")

def main():
    # initialize the parser
    parser = argparse.ArgumentParser(description="Modify your resume/CV to suite the particular job. \
        Give 2 arguments - resume's tex file and a .txt file containing jon description. Like this - \
        python main.py resume.tex JD.txt")
    parser.add_argument("res", help="Name of the .tex file to process")
    parser.add_argument("jd", help="Name of the file that contains job description to process")
    args = parser.parse_args()

    # input the new skills
    new_skills = input("Enter the new skills - ")
    
    # read the files
    tex_path = Path(args.res)
    jd_path = Path(args.jd)
    tex_file = read_file(tex_path)
    jd_file = read_file(jd_path)

    # initialize the llm class
    gemini_llm = GeminiLLM(api_key)

    # get contents out of tex file, job description file and new skills
    contents = gemini_llm.get_contents(tex_file)
    job_descrp = gemini_llm.get_jod_descrp(jd_file)
    new_skills = gemini_llm.get_new_skills(new_skills)

    # save the above outputs for more information
    save_file(contents, "content.txt")
    save_file(job_descrp, "job_descrp.txt")
    save_file(new_skills, "new_skills.txt")

    # get new resume data
    new_resume_data = gemini_llm.get_new_resume_data(contents, job_descrp, new_skills)

    # get new resume file
    new_resume_file = gemini_llm.get_new_resume_file(new_resume_data, tex_file)

    # save the file
    save_file(new_resume_file, "modified_" + args.res)


if __name__ == "__main__":
    main()