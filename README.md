# PLP2 — Group 2 (Education)
A simple command-line (CLI) student management system developed in Python with an SQLite database.

## Description
This program allows a teacher to:
1. Enroll a new student (name, age, grade, attendance)
2. Display the list of all registered students
3. Analyze students as "Good Standing" (average ≥ 75%) vs. "Needs Improvement"
4. Exit the program

## Project Structure
```
plp2-group2/
├── main.py # Entry point: menu, main loop, display, analysis
├── student.py # StudentInfo class + Good Standing rule (75%)
├── database.py # SQLite connection: table creation, adding, loading students
└── README.md
```

## Installation and Launch
```bash
git clone <repo-link>
cd plp2-group2
python main.py

```
No external dependencies: the project uses only the standard Python library (`sqlite3`).

## Usage
On launch, the main menu appears with 4 options:
```
1. Register a student
2. Show all students
3. Analyze students (Good Standing)
4. Exit
```
Choose a number and follow the on-screen instructions. The data is automatically saved to the SQLite database between each session.

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
