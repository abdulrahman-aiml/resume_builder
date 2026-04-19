import os
from crewai import Crew
from docx2pdf import convert
from src.agents import research_agent, resume_builder_agent
from src.tasks import research_task, resume_building_task

def main():
    if not os.path.exists('docs'):
        os.makedirs('docs')

    while True:
        user = input("Enter target role (or 'exit'): ")
        if user.lower() in ['break', 'exit']:
            break
            
        # Dynamically set output file
        filename = f"resume_{user.replace(' ', '_')}"
        resume_building_task.output_file = f"docs/{filename}.docx"
            
        crew = Crew(
            agents=[research_agent, resume_builder_agent],
            tasks=[research_task, resume_building_task],
            verbose=True
        )
        
        print("Starting crew...")
        crew.kickoff(inputs={"role": user})
        
        # Convert the generated docx to pdf
        try:
            print(f"Converting {filename}.docx to PDF...")
            convert(f"docs/{filename}.docx", f"docs/{filename}.pdf")
            print(f"Success! Files saved in docs/ as {filename}.docx and {filename}.pdf")
        except Exception as e:
            print(f"Conversion failed: {e}")

if __name__ == "__main__":
    main()