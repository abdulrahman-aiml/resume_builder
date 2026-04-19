from crewai import Task
from .agents import research_agent, resume_builder_agent

# Task 1: Research industry standards for the target role
research_task = Task(
    description="""Conduct thorough research on the target job role. 
    Analyze the key skills, required certifications, common keywords, 
    and structural preferences (e.g., chronological vs. functional) 
    sought by industry leaders for this specific position.{role}""",
    expected_output="""A comprehensive report detailing the top 5 essential skills, 
    a list of 10 high-value keywords for ATS optimization, and a recommendation 
    on the best resume structure for the target role.""",
    agent=research_agent
)

# Task 2: Build the resume using the research findings
resume_building_task = Task(
    description="""Draft a professional, ATS-optimized resume. Incorporate 
    the skills and keywords identified in the research phase. 
    Structure the document for maximum impact.""",
    expected_output="A professionally written resume.",
    agent=resume_builder_agent,
    context=[research_task],
    output_file="docs/resume.docx" # CrewAI will create this file
)