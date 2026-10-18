import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from bs4 import BeautifulSoup

# =========================================================
# SECTION 1: CONFIGURATION & VIEW STATE
# =========================================================
st.set_page_config(page_title="Curriculum Architecture Engine", layout="wide")

st.title("🏗️ Curriculum Architecture Engine")
st.caption("Autonomous Pathway Alignment, Dynamic Gap Extraction & Cohort Pacing")

# Target Audience / View Mode Switch
view_mode = st.radio(
    "View Mode:",
    ["LX Designer / Admin View", "Learner Cohort View"],
    horizontal=True
)

st.divider()

# =========================================================
# SECTION 2: DATA REGISTRIES
# =========================================================
@st.cache_data
def load_capstone_registry():
    return pd.DataFrame([
        {
            "Capstone_ID": "CAP-FED-01",
            "Title": "Front-End Web Application Capstone",
            "Domain": "Web Development",
            "Required_Skills": ["React", "JavaScript ES6", "REST APIs", "Responsive UI/UX", "Redux State Management", "Async Error Handling"],
            "Deliverables": [
                "Figma Wireframe & UI Spec",
                "Functional Single-Page React App",
                "API Integration with Fallback Handlers",
                "Unit Test Suite (Jest/RTL)"
            ],
            "Est_Effort_Hours": 25
        },
        {
            "Capstone_ID": "CAP-SAP-01",
            "Title": "SAP Technology Consultant Capstone",
            "Domain": "Enterprise Systems",
            "Required_Skills": ["SAP S/4HANA Cloud", "Fit-to-Standard", "Business Case Framing", "Cloud Deployment Models"],
            "Deliverables": [
                "Fit-to-Standard Discovery Plan",
                "Solution Architecture Blueprint",
                "Sustainability ROI Model"
            ],
            "Est_Effort_Hours": 20
        }
    ])

@st.cache_data
def load_coursera_profiles():
    return {
        "Meta Front-End Developer": {
            "Covered_Skills": ["HTML5/CSS3", "JavaScript Basics", "React Components", "Git/GitHub", "UX Fundamentals"],
            "Base_Hours": 24
        },
        "IBM Project Manager": {
            "Covered_Skills": ["Project Charters", "Agile/Scrum Basics", "Risk Analysis", "Stakeholder Communication"],
            "Base_Hours": 20
        }
    }

capstone_df = load_capstone_registry()
coursera_profiles = load_coursera_profiles()

# =========================================================
# SECTION 3: SIDEBAR CONTROLS
# =========================================================
st.sidebar.header("⚙️ Cohort & Engine Controls")

selected_cert = st.sidebar.selectbox(
    "Select Coursera Certificate Pathway",
    list(coursera_profiles.keys())
)

def format_capstone_label(cap_id):
    row = capstone_df[capstone_df["Capstone_ID"] == cap_id]
    return f"{cap_id} - {row['Title'].values[0]}"

selected_capstone_id = st.sidebar.selectbox(
    "Select Target Capstone",
    capstone_df["Capstone_ID"].tolist(),
    format_func=format_capstone_label
)

max_weekly_hours = st.sidebar.slider("Max Learner Weekly Capacity (Hours)", 8, 20, 10)
start_date = st.sidebar.date_input("Cohort Start Date", pd.to_datetime("2026-09-01"))
cohort_classroom_url = st.sidebar.text_input("Active Google Classroom Link", "https://classroom.google.com/c/web-dev-2026-a")

# =========================================================
# SECTION 4: AGENTIC GAP ANALYSIS ENGINE (DYNAMIC CALCULATIONS)
# =========================================================
coursera_data = coursera_profiles[selected_cert]
capstone_data = capstone_df[capstone_df["Capstone_ID"] == selected_capstone_id].iloc[0]

covered_set = set(coursera_data["Covered_Skills"])
required_set = set(capstone_data["Required_Skills"])

# Autonomous Gap Calculation
missing_competencies = list(required_set - covered_set)
overlap_competencies = list(required_set.intersection(covered_set))

# Calculate Gap Severity Index (0.0 to 1.0)
gap_severity = len(missing_competencies) / len(required_set) if required_set else 0

# =========================================================
# SECTION 5: DYNAMIC TIMELINE RE-BALANCING
# =========================================================
st.header("1. Automated Pathway Schedule & Adaptive Pacing")

# Build schedule dynamically based on gap severity
schedule_blocks = [
    {"Activity": f"{selected_cert}: Core Foundations", "Category": "Self-Paced", "Hours": 8},
    {"Activity": f"{selected_cert}: Applied Labs", "Category": "Self-Paced", "Hours": 8},
]

# If gap severity is high, automatically inject targeted enrichment workshops
if gap_severity > 0.3:
    schedule_blocks.append({
        "Activity": f"Enrichment Workshop 1: Deep-Dive on {missing_competencies[0] if missing_competencies else 'Advanced Topics'}",
        "Category": "Live SME Session",
        "Hours": 3
    })

if len(missing_competencies) > 1:
    schedule_blocks.append({
        "Activity": f"Enrichment Workshop 2: Mastering {missing_competencies[1]}",
        "Category": "Live SME Session",
        "Hours": 3
    })

schedule_blocks.extend([
    {"Activity": f"Capstone Execution: {capstone_data['Title']}", "Category": "Project", "Hours": capstone_data["Est_Effort_Hours"] / 2},
    {"Activity": "Capstone Finalization & Submission", "Category": "Project", "Hours": capstone_data["Est_Effort_Hours"] / 2},
    {"Activity": "Peer Review & Evaluation Window", "Category": "Evaluation", "Hours": 3}
])

# Re-balance activities across weeks according to weekly hour capacity
current_week = 1
current_week_hours = 0
week_assignments = []

for block in schedule_blocks:
    if current_week_hours + block["Hours"] > max_weekly_hours and current_week_hours > 0:
        current_week += 1
        current_week_hours = 0
    
    week_assignments.append({
        "Week": current_week,
        "Activity": block["Activity"],
        "Category": block["Category"],
        "Hours": block["Hours"],
        "Start_Date": start_date + pd.Timedelta(weeks=current_week - 1),
        "End_Date": start_date + pd.Timedelta(weeks=current_week - 1, days=6)
    })
    current_week_hours += block["Hours"]

schedule_df = pd.DataFrame(week_assignments)

# Render Plotly Gantt Chart with Legend Positioned ABOVE the Chart
fig = px.timeline(
    schedule_df,
    x_start="Start_Date",
    x_end="End_Date",
    y="Activity",
    color="Category",
    title=f"Adaptive Timeline: {selected_cert} ➔ {capstone_data['Title']}"
)
fig.update_yaxes(autorange="reversed")
fig.update_layout(
    height=450,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)
st.plotly_chart(fig, use_container_width=True)

# Weekly Workload Summary Metrics
weekly_summary = schedule_df.groupby("Week")["Hours"].sum().reset_index()
st.subheader("Weekly Workload Capacity Monitor")

cols = st.columns(min(len(weekly_summary), 8))
for idx, row in weekly_summary.iterrows():
    if idx < len(cols):
        week_num = int(row["Week"])
        hrs = int(row["Hours"])
        is_overload = hrs > max_weekly_hours
        cols[idx].metric(
            label=f"Week {week_num}",
            value=f"{hrs} hrs",
            delta=f"{hrs - max_weekly_hours} hrs" if is_overload else "Balanced",
            delta_color="inverse" if is_overload else "normal"
        )

st.divider()

# =========================================================
# SECTION 6: ROLE-BASED CONDITIONAL VIEWS
# =========================================================
if view_mode == "LX Designer / Admin View":
    st.header("2. AI Gap Analysis & SME Facilitation Brief")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Coursera Covered Skills")
        st.info(", ".join(coursera_data["Covered_Skills"]))

    with col2:
        st.subheader("Capstone Target Skills")
        st.success(", ".join(capstone_data["Required_Skills"]))

    st.markdown("### 🔍 Automated Competency Gap Assessment")
    
    gap_col1, gap_col2 = st.columns(2)
    
    with gap_col1:
        st.markdown("**Identified Deliverable Gaps:**")
        for deliverable in capstone_data["Deliverables"]:
            st.markdown(f"- {deliverable}")

    with gap_col2:
        st.markdown("**Missing Critical Competencies:**")
        if missing_competencies:
            for missing in missing_competencies:
                st.markdown(f"  - ⚠️ **{missing}** (Requires SME intervention)")
        else:
            st.markdown("  - ✅ No critical skill gaps identified!")

    st.markdown("---")
    st.subheader("📋 Recommended Multi-Session SME Facilitation Plan")
    st.caption("Auto-generated based on current gap severity score.")

    if missing_competencies:
        for idx, missing in enumerate(missing_competencies, 1):
            with st.expander(f"Session {idx}: Deep-Dive on {missing}", expanded=True):
                st.markdown(f"""
                * **Objective:** Bridge the target competency gap in **{missing}** required for *{capstone_data['Title']}*.
                * **Suggested SME Agenda:**
                  1. **00–15m:** Theoretical Context & Architecture Overview.
                  2. **15–35m:** Live Pair-Coding / Walkthrough of edge cases.
                  3. **35–50m:** Reviewing Capstone rubric expectations for {missing}.
                  4. **50–60m:** Q&A and assignment of practice drills.
                """)
    else:
        st.success("Pathway fully aligned! Standard Q&A check-ins recommended.")

elif view_mode == "Learner Cohort View":
    st.header("2. Student Learning Resources & Links")
    st.info("Welcome to your cohort dashboard! Use the links below to access your workspace and submit milestones.")
    
    l_col1, l_col2 = st.columns(2)
    with l_col1:
        st.link_button("🚀 Launch Google Classroom", cohort_classroom_url, use_container_width=True)
    with l_col2:
        st.link_button("📁 Open Capstone Workspace", f"{cohort_classroom_url}/p/capstone", use_container_width=True)