import datetime
from openpyxl import Workbook
import os

WEEKLY_HOURS = 20

COURSES = [
    ("Berechenbarkeit und Komplexität", 5),
    ("Kommunikationsnetze", 4),
    ("Stochastik", 4),
    ("Requirements Engineering", 3),
    ("Wahlpflichtmodul I", 3),
]
STAGE_WEIGHT = {
    "early": 1.0,
    "mid": 1.5,
    "final": 2.5
}


def get_stage(semester):
    month = datetime.datetime.now().month
    if semester == "winter":
        if month <= 11:
            return "early"
        elif month == 12:
            return "mid"
        else:
            return "final"

    if semester == "summer":
        if month <= 5:
            return "early"
        elif month == 6:
            return "mid"
        else:
            return "final"


def generate_plan(stage):
    weighted = []
    total = 0

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


semester = input("Which semester? (winter/summer): ").strip().lower()
stage = get_stage(semester)

plan = generate_plan(stage)
export_excel(plan, stage)
print("Excel created: study_plan.xlsx")


def explain_plan(plan, stage):
    print("\nAssistant:")
    print(f"You are currently in the {stage} phase of the semester.")
    print("Here is your optimized study plan:")

    for course, hours in plan:
        print(f"- Focus on {course} for about {hours} hours this week.")

    print("\nTip: Let me know next week how it went, and I will adjust your plan.")


explain_plan(plan, stage)
