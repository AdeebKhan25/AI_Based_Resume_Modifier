from google import genai
from google.genai import types


class GeminiLLM:
    """
    LLM class for handling LLM functionalities
    """
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-3-flash-preview"

    def get_response(self, system_instruction, prompt, data):
        response = self.client.models.generate_content(
            model=self.model,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction),
            contents= prompt + data
        )
        return response.text

    def get_contents(self, file_data):
        system_instruction = "You are a text content parser, especially a .tex file parser. \
            You take the data given as prompt - which is a .tex file and extract all the data out of it excluding .tex elements and tags. \
            You always make sure that no data/information is lost. \
            The .tex files you process is a resume/CV files, so you process them accordingly."
        prompt = "Parse and store the contents of given resume/CV .tex file "
        contents = self.get_response(system_instruction=system_instruction, prompt=prompt, data=file_data)
        return contents

    def get_jod_descrp(self, job_data):
        system_instruction = "You are a technincal recruiter/very experienced engineer (from FAANG\ Big tech\ Great Startups) who interviews a lot of people. \
            You take a job description as input and tell what is actually being demanded from job candidate. \
            You take away superfluos jargon away and boil down things to simplest. \
            You tell what is expected and really required, \
            and most important what you want to see in candidate resume that will delight your eyes and you say this is what I want \
            and this is the person I am looking for."
        prompt = "Take the following job description and tell me what is recruiter actually looking for."
        job_descrp = self.get_response(system_instruction=system_instruction, prompt=prompt, data=job_data)
        return job_descrp

    def get_new_skills(self, skills):
        system_instruction = "You are a very highly experienced engineer (from FAANG\ Big tech\ Great Startups) who interviews a lot of people. \
            You yourself have cracked dozen of interviews and hiring assessments. \
            Given a set of skill ideas you can change them in perfect points in resume/CV, that catches the eyes of recruiters."
        prompt = "Given following skill ideas, create perfect resume/CV points from it. Also, tell where they should be added or how they can \
            be showcased to recruiter - in form of projects, experience, open-source contribution, research, etc. (Projects will be more preferred)"
        new_skills = self.get_response(system_instruction=system_instruction, prompt=prompt, data=skills)
        return new_skills

    def get_new_resume_data(self, contents, job_descrp, new_skills=""):
        system_instruction = "You are a very highly experienced engineer (from FAANG\ Big tech\ Great Startups) who interviews a lot of people. \
            You yourself have cracked dozen of interviews and hiring assessments. \
            You are an expert/master in creating the most perfect resumes/CV tailored to the required jobs."
        prompt = f"Create the most elegant and perfect resume/CV you can from following data. \
            Take the information from current resume, which is as follows: {contents}. \
            Now, modify this data in light of following data from job description: {job_descrp}. \
            Also, there may be some new skills that author want to add which is as follows (It maybe empty): {new_skills}"
        new_resume_data = self.get_response(system_instruction=system_instruction, prompt=prompt, data="")
        return new_resume_data

    def get_new_resume_file(self, new_resume_data, file_data):
        system_instruction = "You are a text editor, especially a .tex file editor. \
            You specialize in editing the .tex files."
        prompt = f"Take the old .tex file {file_data} and change the data fields according to {new_resume_data}. Make sure that \
            in no way the structure of the resulting file changes. Lookwise they should look same except contents would be different. \
            So, focus on the fact the .tex elements and tags remain as such so \
            the only difference in old .tex file and new .tex file is that of data fields. This output should be clean .tex file, nothing extra."
        new_resume_file = self.get_response(system_instruction=system_instruction, prompt=prompt, data="")
        return new_resume_file