from app.matcher import calculate_match_score
from app.job_parser import parse_job_description,job_description
from app.resume_parser import parse_resume
from app.readers import read_resume
from pathlib import Path

resume_path = Path("C:/Users/TANMAY/Downloads/CV-hrithik.pdf")
resume_text = read_resume(resume_path)
resume = parse_resume(resume_text)
job = parse_job_description(job_description)  # hardcoded JD
result = calculate_match_score(job, resume)
print(result)