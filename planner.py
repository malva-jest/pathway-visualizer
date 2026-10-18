import pandas as pd

import os
from google import genai
import json


def generate_cohort_schedule(start_date, weekly_study_pace):
    """
    Calculates deterministic pacing rules:
    - Component study steady-state
    - 3-Day Praxis Sprints
    - Month-end Capstone + Peer Review + AI Regrade Buffer
    """
    schedule = [
        {"Week": 1, "Activity": "Coursera: HTML5 & CSS3 Basics", "Type": "Component", "Hours": 8},
        {"Week": 2, "Activity": "Coursera: JavaScript ES6 & DOM", "Type": "Component", "Hours": 10},
        {"Week": 3, "Activity": "Praxis Sprint: Stakeholder Communication (3 Days)", "Type": "Praxis", "Hours": 6},
        {"Week": 3, "Activity": "Coursera: React Fundamentals (Light Pace)", "Type": "Component", "Hours": 4},
        {"Week": 4, "Activity": "Capstone Execution: Front-End App", "Type": "Capstone", "Hours": 15},
        {"Week": 4, "Activity": "Peer Review Window & AI Feedback Regrade", "Type": "Evaluation", "Hours": 4}
    ]

    
    df = pd.DataFrame(schedule)
    df["Start_Date"] = df["Week"].apply(lambda w: start_date + pd.Timedelta(weeks=w - 1))
    df["End_Date"] = df["Start_Date"] + pd.Timedelta(days=6)
    return df


# def build_capstone_prompt(role: str, gap_skills: list[str]) -> str:
#     """
#     Formats target role and missing skills into a structured JSON prompt template for LLM generation.
#     """
#     skills_formatted = ", ".join(gap_skills)

#     prompt = f"""
# SYSTEM INSTRUCTION: You are an expert Curriculum Designer.
# Generate a real-world Capstone Project scenario tailored for a learner targeting the role of '{role}'.

# TARGET ROLE: {role}
# GAPS TO ADDRESS: {skills_formatted}

# Return ONLY valid JSON in the following format:
# {{
#     "title": "Project Title",
#     "scenario": "Scenario description...", 
#     "deliverables": ["Deliverables 1", "Deliverables 2"]
# }}
# """
#     return prompt



# test_prompt = build_pstone_prompt("Data Engineer", ["Python OOP", "SQL", "Docker"])
# print(test_prompt)


# interaction = client.interactions.create(
#     model="gemini-3.8-flash",
#     system_instruction="You are a cat. Your name is Neko.",   --------> USEFUL
#     input="Hello there"
# )

# def generate_capstone_project(role: str, gap_skills: list[str]) -> dict:
    
#     prompt_text = build_capstone_prompt(role, gap_skills)
#     client = genai.Client(GEMINI_API_KEY)
#     # Generate the content
#     response = client.models.generate_content(
#         model='gemini-2.5-flash',
#         contents=prompt_string,
# )
#     # parse response:
#     parsed_response = json.loads(response.text)

#     # Print the parsed generated text output
#     print parsed_response

