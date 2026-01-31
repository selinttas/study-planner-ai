import datetime
import os

import streamlit
import streamlit as st
from openpyxl import Workbook

WEEKLY_HOURS = 20

COURSES = [
    ("Berechenbarkeit und Komplexität", 5),
    ("Kommunikationsnetze", 4),
    ("Stochastik", 4),
    ("Requirements Engineering", 3),
    ("Wahlpflichtmodul I", 3),
]

STAGE_WEIGHT = {"early": 1.0, "mid": 1.5, "final": 2.5}

def get_stage(semester):
    month = datetime.datetime.now().month
    if semester == "winter":
        if month <= 11: return "early"
        elif month == 12: return "mid"
        else: return "final"
    if semester == "summer":
        if month <= 5: return "early"
        elif month == 6: return "mid"
        else: return "final"

def generate_plan(stage):
    weighted, total = [], 0
    for name, diff in COURSES:
        score = diff * STAGE_WEIGHT[stage]
        weighted.append((name, score))
        total += score

    plan = []
    for name, score in weighted:
        hours = round((score / total) * WEEKLY_HOURS, 1)
        plan.append((name, hours))
    return plan

def export_excel(plan, stage):
    wb = Workbook()
    ws = wb.active
    ws.title = "Study Plan"
    ws.append(["Course", "Hours per Week", "Stage"])
    for course, hours in plan:
        ws.append([course, hours, stage])
    path = os.path.join(os.getcwd(), "study_plan.xlsx")
    wb.save(path)
    return path

# ---------- UI ----------
st.title("🎓 Study Planner AI")

semester = st.selectbox("Which semester are you in?", ["winter", "summer"])

if st.button("Generate my plan"):
    stage = get_stage(semester)
    plan = generate_plan(stage)
    path = export_excel(plan, stage)

    st.success(f"You are in the **{stage}** phase.")
    st.subheader("Your weekly plan:")
    for c, h in plan:
        st.write(f"• **{c}** → {h} hours")

    with open(path, "rb") as f:
        st.download_button(
            label="⬇️ Download Excel",
            data=f,
            file_name="study_plan.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
