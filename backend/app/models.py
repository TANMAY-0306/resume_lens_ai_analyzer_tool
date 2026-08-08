from pydantic import BaseModel, Field

class JobDescription(BaseModel):
    role: str
    required_skills: list[str] = Field(default_factory=list)
    preferred_skills: list[str] = Field(default_factory=list)
    minimum_experience: float | None = None
    educational_requirements: list[str] = Field(default_factory=list)
    responsibilities: list[str] = Field(default_factory=list)

class Experience(BaseModel):
    company: str | None = None
    role: str | None = None
    duration: str | None = None
    description: str | None = None
    skills_used: list[str] = Field(default_factory=list)

class Resume(BaseModel):
    name: str | None = None
    email: str | None = None
    phone_number: str | None = None
    total_experience: float | None = None
    skills: list[str] = Field(default_factory=list)
    experiences: list[Experience] = Field(default_factory=list)
    projects: list[str] = Field(default_factory=list)
    certificates: list[str] = Field(default_factory=list)

class MatchDetails(BaseModel):
    candidate_name: str | None = None
    matching_skills: list[str] = Field(default_factory=list)
    missing_skills: list[str] = Field(default_factory=list)
    experience_requirement_met: bool
    education_requirement_met: bool 
    strengths: list[str] = Field(default_factory=list)
    suggestions: list[str] = Field(default_factory=list)
    verdict: str

class MatchResult(BaseModel):
    job_match_score: float = Field(ge=0, le=100)
    details: MatchDetails

#JSON SCHEMAS
jobd_schema=JobDescription.model_json_schema()
resume_schema=Resume.model_json_schema()
