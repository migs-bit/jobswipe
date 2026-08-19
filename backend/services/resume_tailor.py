from openai import OpenAI
from dotenv import load_dotenv
from config.settings import settings

load_dotenv()

prompt = """
You are a resume analysis assistant. You will be given a resume and a job 
description. Your job is to provide specific, actionable suggestions for 
how the candidate could better tailor their resume to this specific job.

Rules:
- Only suggest changes based on what's actually in the resume — never invent 
  experience, skills, or qualifications
- Focus on: keyword alignment, reordering bullets by relevance, highlighting 
  transferable skills
- Provide 5-7 specific, actionable bullet points
- Keep each suggestion concise — one to two sentences
- Do not rewrite the entire resume, only suggest what to change and why
"""

def analyze_resume(resume_text: str, job_description: str) -> str:
    client = OpenAI(
        api_key=settings.DEEPSEEK_API_KEY,
        base_url=settings.DEEPSEEK_BASE_URL
    )

    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        max_tokens=2000,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"resume: {resume_text}\n\nJob: {job_description}"}
        ],
        stream=False,
        reasoning_effort='high',
        extra_body={"thinking": {"type": "disabled"}}
    )
    print("FULL RESPONSE:", response)

    return response.choices[0].message.content