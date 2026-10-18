import pandas as pd

def load_component_registry():
    """Mock registry of Coursera modules/components."""
    return pd.DataFrame([
        {"Component_ID": "COMP-FE-01", "Domain": "Web Development", "Title": "HTML5 & CSS3 Basics", "Est_Hours": 8},
        {"Component_ID": "COMP-FE-02", "Domain": "Web Development", "Title": "JavaScript ES6 & DOM", "Est_Hours": 10},
        {"Component_ID": "COMP-FE-03", "Domain": "Web Development", "Title": "React Fundamentals", "Est_Hours": 12},
        {"Component_ID": "COMP-FE-04", "Domain": "Web Development", "Title": "Async JS & REST APIs", "Est_Hours": 10}
    ])

def load_capstone_registry():
    """Mock registry of existing capstones."""
    return pd.DataFrame([
        {
            "Capstone_ID": "CAP-FED-01",
            "Domain": "Web Development",
            "Title": "Front-End Web Application Capstone",
            "Target_Skills": "React, JavaScript ES6, REST APIs, State Management",
            "Est_Hours": 20
        }
    ])

def load_praxis_registry():
    """Mock registry of 3-day Praxis workplace scenarios."""
    return pd.DataFrame([
        {
            "Scenario_ID": "PRX-COMM-01",
            "Domain": "Web Development",
            "Title": "Explaining Technical Trade-offs to Stakeholders",
            "Est_Hours": 6
        }
    ])