# 🎓 Study Planner AI

A proactive, web-based AI study planner for Software Engineering students in Germany.  
The assistant automatically generates adaptive weekly study schedules based on
course difficulty, semester phase, and the German single-exam academic system.

---

## 🚀 Features

- Detects semester phase automatically (early / mid / final)
- Prioritizes courses by difficulty
- Generates a personalized weekly study plan (20h/week)
- Exports the plan to Excel
- Web interface built with Streamlit

---

## 🧠 How it works

1. User selects semester (winter / summer)
2. System detects academic phase from current date
3. Weighted algorithm distributes weekly hours
4. Plan is displayed and exported as an Excel file

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- OpenPyXL  

---

## ▶️ Run locally

```bash
pip install streamlit openpyxl
streamlit run app.py
