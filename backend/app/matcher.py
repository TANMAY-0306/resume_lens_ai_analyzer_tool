import json
from app.config import client, model
from app.models import MatchResult ,Resume,JobDescription

match_schema=MatchResult.model_json_schema()
def calculate_match_score(job:JobDescription,resume:Resume):
    ''' model_dump_json() converts the Pydantic object into a JSON string.
     This allows the LLM to receive the job description in a structured format.'''
    
    prompt = f"""
        You are an HR recruiter.

        Compare the candidate's resume with the job description.

        JOB DESCRIPTION:
        {job.model_dump_json(indent=2)}                        

        CANDIDATE RESUME:
        {resume.model_dump_json(indent=2)}
        Return JSON matching this schema:

        {match_schema}

        Give me:
        1. Candidate name
        2. Matching skills
        3. Missing important skills
        4. Whether experience requirement is met
        5. Whether education requirement is met
        6. Candidate strengths
        7. Suggestions for improvement
        8. Final verdict
        9. Overall match percentage (0–100)
        Keep the response concise and easy to read.
        Rules:
        1. experience_requirement_met must always be true or false.
        2. education_requirement_met must always be true or false.
        3. Never return null for these fields.
        4. If no minimum years of experience are specified in the job description, set experience_requirement_met to true.
        5. If educational requirements are met, set education_requirement_met to true, otherwise false.
            """
    user_message={
        "role":"user",
        "content":prompt
    }
    system_message = {
    "role": "system",
    "content": "You are an expert HR recruiter."
}

    messages = [system_message, user_message]
    response_format={
        "type":"json_object"
    }
    messages=[user_message]
    response=client.chat.completions.create(model=model,response_format=response_format,messages=messages)
    response_content=response.choices[0].message.content
    data_json=json.loads(response_content)
    match_result=MatchResult(**data_json)
    return match_result
