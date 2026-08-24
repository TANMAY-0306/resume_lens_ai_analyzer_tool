from app.matcher import calculate_match_score
from app.job_parser import parse_job_description
from app.resume_parser import parse_resume
from app.readers import read_resume
from app.models import MatchResult
from pathlib import Path

# resume_path = Path("C:/Users/TANMAY/Downloads/CV-hrithik.pdf")
# resume_text = read_resume(resume_path)
# resume = parse_resume(resume_text)
# job = parse_job_description(job_description)  # hardcoded JD
# result = calculate_match_score(job, resume)
# print(result)
from fastapi import FastAPI ,UploadFile,Form,File

app=FastAPI()
@app.post("/analyze" ,response_model=MatchResult)
async def analyze(
    resume_file:UploadFile=File(),
    job_description:str=Form()
):

    resume = parse_resume(...)

    job = parse_job_description(...)

    result = calculate_match_score(
        job,
        resume
    )

    return result