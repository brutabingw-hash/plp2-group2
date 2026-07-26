PLP2 — Group 2 (Education)
Simple command line (CLI) student management system, developed in Python with an SQLite database.

Description
This program allows a teacher to:
Register a new student (name, age, grade/level, attendance rate)
View list of all registered students
Analyze students in “Good Standing” vs “Needs Improvement” according to their attendance rate
Update an existing student's information
Delete a student
Exit the program
Project structure
plp2-group2/
├── main.py # Entry point: menu, main loop, display, analysis
├── student.py # StudentInfo class + Good Standing rule (75%)
├── database.py # SQLite connection: create table, add, update, delete, load students
└── README.md
Installation and launch
bash
git clone <repo-link>
cd plp2-group2
python main.py

No external dependencies: the project only uses the standard Python library (sqlite3).
Use
When launched, the main menu is displayed with 6 options:

=========================================================== 
Student Online Record-Keeping System
===========================================================

Welcome to the Student Online Record-Keeping System!
Please choose an option:
1. Register a Student
2. View Student Records
3. Student Records Analysis
4. Update a Student
5. Delete a Student
6. Exit

Choose a number and follow the on-screen instructions. The data is automatically saved in the SQLite database between each session.

## Team and Task Allocation
| Member | Contribution |
|---|---|
| Blair | Setting up the repository, initial structure |
| Grace | Main menu (`print_menu()`) |
| Hassan | Student registration (`student_registration()`) |
| Joy | `StudentInfo` class and Good Standing rule (`student.py`) |
| Ismael | SQLite integration (`database.py`) and main loop (`main()`) |
| Christa | Displaying students (`display_students()`) and tests |
| Rosanne | Demonstration, screenshots, user flow diagram |

## Database
All data is stored in an SQLite database (no CSV/JSON files), with a `students` table containing: name, age, grade, attendance.

## License

This project is an academic project completed as part of the Peer Learning Project I
