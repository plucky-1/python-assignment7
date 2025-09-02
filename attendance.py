"""
Attendance Register

Task:
- Track attendance of students.
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports.
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True).

// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.
"""

import datetime

attendance = {}

def register_student(student_id, name):
    """Register a student in the system."""
    attendance[student_id] ={"name":name,"present_days":[],"absent_days":[]}

def mark_present(student_ids):
    """Mark multiple students as present for today."""
    today = str(datetime.date.today())
    for student in attendance:
        if student not in attendance[student]["present_days"]:
            attendance[student]["present_days"].append(today)

        if today in attendance[student]["absent_days"]:
            attendance[student]["absent_days"].remove(today)
    

def mark_absent(student_ids):
    """Mark multiple students as absent for today."""
    today = str(datetime.date.today())
    for student in student_ids:
        if today not in attendance:
            if today not in attendance[student]["absent_days"]:
                if today not in attendance["absent_days"]:
                    attendance[student]["absent_days"].append(today)
                if today in attendance[student]["present_days"]:
                    attendance[student]["present_days"].remove(today)
    

def get_report(**kwargs):
    """Generate attendance report with optional filters."""
    report = {}
    present_students =kwargs.get("present_students",False)
    absent_students = kwargs.get("absent_students",False)
    for student, info in attendance.items():
        if present_students and not info["present_days"]:
            continue
    return report

