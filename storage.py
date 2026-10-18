import json
import os

STORAGE_FILE = "saved_cohorts.json"

def save_cohort_timeline(cohort_id, schedule_data):
    """Saves a finalized cohort timeline to local JSON storage."""
    cohorts = load_all_cohorts()
    cohorts[cohort_id] = schedule_data
    with open(STORAGE_FILE, "w") as f:
        json.dump(cohorts, f, indent=4)

def load_all_cohorts():
    """Loads all saved cohort timelines."""
    if not os.path.exists(STORAGE_FILE):
        return {}
    with open(STORAGE_FILE, "r") as f:
        return json.load(f)

def load_single_cohort(cohort_id):
    """Retrieves a specific cohort's locked schedule."""
    cohorts = load_all_cohorts()
    return cohorts.get(cohort_id, None)