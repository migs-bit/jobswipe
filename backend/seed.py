from database import SessionLocal, engine, Base
from models.job import Job
from models.user import User

Base.metadata.create_all(bind=engine)

jobs = [
        {"title": "jr software engineer", "company": "Google", "location": "San Francisco","salary": "80k-120k", "description": """Job Description

The Opportunity

The Software Engineering Intern- Python Modernization & Automation will support Product Engineering initiatives focused on modernizing and improving critical software tools used in manufacturing and test-floor operations.

This role will primarily focus on converting legacy Python 2.7 analysis scripts to Python 3.x, improving code maintainability, enhancing deployment processes, and helping prepare the software for global manufacturing use. These tools are essential to automated data analysis and results reporting for multiple product lines, including DynaCool, OptiCool, VersaLab, and MPMS3 systems.

Responsibilities

Analyze and convert existing Python 2.7 scripts to Python 3.x.
Verify software functionality following migration through unit testing and regression testing.
Refactor and modularize existing code to improve maintainability, scalability, and reuse.
Improve code documentation, comments, and developer resources.
Support migration of software assets from Subversion (SVN) to Git-based version control.
Create and maintain deployment and installation procedures for test-floor users.
Participate in the development of automation tools to streamline software deployment and maintenance.
Collaborate with engineers and test technicians to identify opportunities for usability improvements.
Perform code reviews, testing, debugging, and troubleshooting activities.
Develop recommendations and processes to keep the codebase current with future Python releases.
Participate in design reviews and present technical recommendations to stakeholders.
Support additional software enhancement projects as time allows.

Qualifications

Currently pursuing a bachelor’s degree in computer science, software engineering, data science, or a related field with two years of completed coursework
Experience coding projects in the Python language

Soft Skills

Strong written and verbal communication skills
Ability to present technical solutions and recommendations in small group settings
Strong attention to detail and commitment to writing well-documented, maintainable code
Excellent problem solving and analytical skills
Ability to work independently while collaborating effectively with cross-functional teams

What You’ll Gain

Real-world experience modernizing a production engineering software environment
Hands-on exposure to software architecture, version control, deployment automation, and testing
Experience collaborating with engineers, technicians, and manufacturing teams
Opportunities to lead an impactful software modernization effort
Experience working with critical tools used in scientific and manufacturing operations
Practical applications of software engineering best practices in a production environment

Additional Information

This position’s work mode is onsite. The employee will report to San Diego, CA
This internship begins in Summer 2026 and may continue into the Fall semester based on business needs and the intern's availability
Hourly: $32 - $38, actual compensation may vary based on education, experience, skills, and qualifications

Quantum Design is an affirmative action and equal opportunity employer. All employment decisions, policies and practices are in accordance with applicable federal, state and local anti-discrimination laws. Quantum Design will not tolerate or engage in unlawful discrimination including any form of unlawful harassment, on account of a person's sex, age, race, color, religion, creed, sexual preference or orientation, marital status, national origin, ancestry, citizenship, military status, veteran status, handicap, disability, or membership in any protected group.""", "tags": "DSA, Python, Kupernetizes" },
        {"title": "developer intern", "company": "Tik Tok", "location": "Houston","salary": "competitive", "description": "your gonna be coding bro, $20/hour", "tags": "DSA, Python, Kupernetizes" },
        {"title": "data anaylst", "company": "Amazon", "location": "New York City","salary": "DOE", "description": "your gonna be coding bro, $45/hour", "tags": "DSA, Python, Kupernetizes" },
        {"title": "SW engineering intern", "company": "Roblox", "location": "Los Angeles","salary": "$150,000 - $200,000", "description": "your gonna be coding bro, $60/hour", "tags": "DSA, Python, Kupernetizes" }
    ]

db = SessionLocal()

try:
    if db.query(Job).first():
        print("Database already seeded, skipping")
        db.close()
        exit()
    job_instance = [Job(**row) for row in jobs]
    db.add_all(job_instance)
    db.commit()
finally:
    db.close()