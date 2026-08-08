import json
from app.config import client, model
from app.models import Resume,resume_schema

def parse_resume(resume_text:str):
    system_prompt=f""" 
    You are an expert resume parser.

        Extract information from the resume based on its meaning,
        not only based on exact section headings.

        Different resumes may use different headings.

        For example:
        - Experience
        - Professional Experience
        - Work History
        - Employment
        - Internships

        These may all contain relevant experience.

        Skills may also appear in the skills section, work experience,
        internships or projects.

        Return ONLY valid JSON matching this schema:

        {resume_schema}

        Important rules:

        1. Do not invent information.
        2. If a value is not available, return null.
        3. If a list has no information, return an empty list.
        4. Include internships inside experiences.
        5. Extract skills mentioned across the entire resume.
        """
    user_prompt=f"""
    Parse the following resume:
    {resume_text}
    """
    system_message={
        "role":"system",
        "content":system_prompt
    }
    user_message={
        "role":"user",
        "content":user_prompt
    }
    response_format={
        "type":"json_object"
    }
    messages=[system_message,user_message]
    response=client.chat.completions.create(model=model,response_format=response_format,messages=messages)
    response_content=response.choices[0].message.content
    json_data=json.loads(response_content)
    resume=Resume(**json_data)
    return resume
