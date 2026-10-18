import streamlit as st
import pandas as pd
import plotly.express as px
from registries import load_capstone_registry, load_component_registry
from planner import generate_cohort_schedule
from storage import save_cohort_timeline, load_all_cohorts, load_single_cohort
from planner import build_capstone_prompt, generate_capstone_project

st.set_page_config(page_title="Curriculum Architecture Engine", layout="wide")

st.title("🏗️ Curriculum Architecture Engine")

# View Switcher
view_mode = st.radio("Access Level:", ["LX Admin", "Learner View"], horizontal=True)
st.divider()

if view_mode == "LX Admin":
    st.header("LX Admin: Cohort Architecture & Pacing")
    
    col1, col2 = st.columns(2)
    with col1:
        cohort_id = st.text_input("Cohort Identifier", "web-dev-2026-a")
        start_date = st.date_input("Cohort Start Date", pd.to_datetime("2026-09-01"))
    with col2:
        max_weekly_hours = st.slider("Weekly Learner Hour Limit", 8, 20, 12)
    
    # Generate Schedule
    schedule_df = generate_cohort_schedule(start_date, max_weekly_hours)
    
    # Plotly Timeline
    fig = px.timeline(
        schedule_df,
        x_start="Start_Date",
        x_end="End_Date",
        y="Activity",
        color="Type",
        title=f"Draft Schedule for {cohort_id}"
    )
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(fig, use_container_width=True)
    
    if st.button("Lock & Save Cohort Schedule"):
        save_cohort_timeline(cohort_id, schedule_df.to_dict(orient="records"))
        st.success(f"Cohort '{cohort_id}' locked and saved to database!")

elif view_mode == "Learner View":
    st.header("Learner Portal: Cohort Schedule")
    
    all_cohorts = load_all_cohorts()
    if not all_cohorts:
        st.info("No saved cohorts found. An LX Admin must lock a schedule first.")
    else:
        selected_cohort = st.selectbox("Select Your Cohort:", list(all_cohorts.keys()))
        cohort_data = load_single_cohort(selected_cohort)
        
        if cohort_data:
            df = pd.DataFrame(cohort_data)
            st.subheader(f"Schedule for {selected_cohort}")
            st.dataframe(df[["Week", "Activity", "Type", "Hours", "Start_Date", "End_Date"]], use_container_width=True)


# test_prompt = build_capstone_prompt("Data Engineer", ["Python", "SQL", "Docker"])
# st.code(test_prompt, language="json")


capstone_dict = generate_capstone_project("Data Engineer", ["Python", "SQL", "Docker"])
st.json(capstone_dict) 