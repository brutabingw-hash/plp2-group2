# Student objects and rules
class StudentInfo:
    # Student Data Record Container

    # Attendance set to 85%
    ATTENDANCE_THRESHHOLD = 85.0

    def __init__(self, name: str, age: int, grade: str, attendance: float):
        # Initializes the four student fields
        self.name = name
        self.name = age
        self.grade = grade
        self.attendance = attendance

    def standing(self) -> str:
        # Checks student status against the required attendance threshold.
        if self.attendance >= self.ATTENDANCE_THRESHHOLD:
            return "Good Standing"
        else:
            return "Needs Improvement"
