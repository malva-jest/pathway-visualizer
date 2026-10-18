# from dataclasses import dataclass

# # Version 1: Standard Python Class
# class StandardProject:
#     def __init__(self, title, focus_skill):
#         self.title = title
#         self.focus_skill = focus_skill

# # Version 2: Data Class Decorator
# @dataclass
# class DataClassProject:
#     title: str
#     focus_skill: str

# # Create instances of both
# p1 = StandardProject("Webmaster Dashboard", "React")
# p2 = DataClassProject("Webmaster Dashboard", "React")

# # Print both instance directly to terminal
# print("Standard Class Output:\n", p1)
# print("\n")
# print("DataClass Output\n", p2)

# p1_duplicate = StandardProject("Webmaster Dashboard", "React")
# p2_duplicate = DataClassProject("Webmaster Dashboard", "React")

# print("Standard equality check:", p1 == p1_duplicate)
# print("DataClass equality check:", p2 == p2_duplicate)

# def build_prompt(role, skills):
#     skills_text = ", ".join(skills)

#     prompt = f"""
#     Create a project for a {role}.
#     Focus on these skills: {skills_text}.
#     """
#     return prompt

# output = build_prompt("Data Engineer", ["Python", "SQL", "Docker"])
# print(output)



# def build_pstone_prompt(role: str, gap_skills: list[str]) -> str:
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


# # import pandas as pd
# from datetime import date, timedelta

# def calc_start(week_number, start_date):
#     # TODO: return start_date plus (week_number - 1) weeks using pd.Timedelta
    
#     chosen
#     start_date = pd.Timedelta(6, "D")

#     today = date.today()
#     start = today - timedelta(days=today.weekday())
#     end = start + timedelta(days=6)
#     print("Today: " + str(today))
#     print("Start: " + str(start))
#     print("End: " + str(end))


#     pass



