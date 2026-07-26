
from database import get_all_students, init_db, add_student

from student import StudentInfo


# Hassan   ← he writes student_registration() HERE ==========================================================================
def student_registration():
    print("\n--- Register a New Student ---")

    name = input("Enter student name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    while True:
        age_input = input("Enter student age: ").strip()
        try:
            age = int(age_input)
            if age <= 0:
                print("Age must be a positive whole number.")
                continue
            break
        except ValueError:
            print("Please enter a valid whole number for age.")

    grade = input("Enter student grade: ").strip()
    while not grade:
        print("Grade cannot be empty.")
        grade = input("Enter student grade: ").strip()

    while True:
        attendance_input = input("Enter attendance percentage (0-100): ").strip()
        try:
            attendance = float(attendance_input)
            if not (0 <= attendance <= 100):
                print("Attendance must be between 0 and 100.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for attendance.")

    student = StudentInfo(name, age, grade, attendance)
    add_student(student)
    print(f"\nStudent '{name}' registered successfully!")


# christa  ← she writes display_students() HERE==============================================================================
def display_students():
    ...



# Joy ======================================================================================================================
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






# Grace ================================================================================================================
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

# Ismael ================================================================================================================

def main():
    """Controls the overall program flow using a loop and menu."""
    init_db()
    print("Welcome!")

    while True:
        print_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            student_registration()
        elif choice == "2":
            display_students()
        elif choice == "3":
            analyze_students()
        elif choice == "4":
            print("\nGoodbye! Closing the system.")
            break
        else:
            print("Invalid choice. Please pick a number from 1 to 4.")


if __name__ == "__main__":
    main()

