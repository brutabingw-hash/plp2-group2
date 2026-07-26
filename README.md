# PLP2 — Group 2 (Education)

A simple command-line (CLI) student management system developed in Python with an SQLite database.

## Description

This program allows a teacher to:
1. Register a new student (name, age, grade, attendance)
2. Display the list of all registered students
3. Analyze students as "Good Standing" vs "Needs Improvement" based on attendance
4. Update an existing student's information
5. Delete a student
6. Exit the program

## Project Structure

```
plp2-group2/
├── main.py         # Entry point: menu, main loop, display, analysis
├── student.py      # StudentInfo class + Good Standing rule (75%)
├── database.py     # SQLite connection: table creation, add, update, delete, load students
└── README.md
```

## Installation and Setup

```bash
git clone <repo-link>
cd plp2-group2
python main.py
```
No external dependencies: the project uses only the Python standard library (`sqlite3`).

## Usage
On launch, the main menu displays with 6 options:

```
==========================================
  Student Online Record-Keeping System
==========================================

Welcome to the Student Online Record-Keeping System!

Please choose an option:

1. Register a Student
2. View Student Records
3. Analyse Student Records
4. Update a Student
5. Delete a Student
6. Exit
```
Choose a number and follow the on-screen instructions. Data is automatically saved to the SQLite database between sessions.


## Team and Task Allocation
| Member | Contribution |
|---|---|
| Blair | Setting up the repository, initial structure |
| Grace | Main menu (`print_menu()`) |
| Hassan | Student registration (`student_registration()`) |
| Joy | `StudentInfo` class and Good Standing rule (`student.py`) |
| Ismael | SQLite integration (`database.py`), main loop (`main()`), student update and delete (`update_student()`) |
| Christa | Displaying students (`display_students()`) and tests |
| Rosanne | Demonstration, screenshots, user flow diagram, (`README.md`) |

## Database

All data is stored in an SQLite database (no CSV/JSON files), in a `students` table with the following schema:

```sql
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade TEXT NOT NULL,
    attendance REAL NOT NULL
)
```

The `StudentInfo` class (in `student.py`) models a student with these 4 fields and a `standing()` method that determines whether they are "Good Standing" or "Needs Improvement".

## License

This project is an academic project completed as part of the Peer Learning Project II.
