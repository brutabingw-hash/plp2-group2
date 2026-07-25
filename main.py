
from database import get_all_students

from student import StudentInfo


def analyze_students():
    # Options 3
    print("\n--- Student Records")

    records = get_all_students()

    if not records:
        print("No students records available to analyze.")
        return

    total_students = len(records)
    good_standing_count = 0
    needs_improvement_count = 0

    print("\nDetailed Performance Breakdown:")
    print("-" * 50)

    # Evaluate individual standing
    for student in records:
        status = student.standing()

        if status == "Good Standing":
            good_standing_count += 1
        else:
            needs_improvement_count += 1
        print(f"- {student.name}: {student.attendance:.1f}% ({status})")


    # Print Summary
    print(" STUDENT ANALYSIS SUMMARY")
    print(f"Total Number of Students : {total_students}")
    print(f"Good Standing            : {good_standing_count}")
    print(f"Needs Improvement        : {needs_improvement_count}")


#Welcome screen and main menu (Option display)
def print_menu():
    print("""==========================================
  Student Online Record-Keeping System
==========================================

Welcome to the Student Online Record-Keeping System!

Please choose an option:

1. Register a Student
2. View Student Records
3. Analyse Student Records
4. Exit""")
