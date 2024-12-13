class Student:
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id
        self.__marks = {}

    def input_marks(self, subject, mark):
        """Adds or updates marks for a specific subject."""
        self.__marks[subject] = mark

    def get_marks(self):
        """Returns all marks."""
        return self.__marks

    def get_average(self):
        """Calculates and returns the average mark."""
        if not self.__marks:
            return 0
        return sum(self.__marks.values()) / len(self.__marks)

    def __str__(self):
        """Returns a string representation of the student's details."""
        return f"Student: {self.__name}, ID: {self.__student_id}, Average Mark: {self.get_average():.2f}"


class StudentManager:
    def __init__(self):
        self.__students = []

    def add_student(self, name, student_id):
        """Adds a new student to the system."""
        student = Student(name, student_id)
        self.__students.append(student)

    def find_student(self, student_id):
        """Finds a student by ID."""
        for student in self.__students:
            if student._Student__student_id == student_id:
                return student
        return None

    def list_students(self):
        """Lists all students."""
        for student in self.__students:
            print(student)

# Example usage
if __name__ == "__main__":
    manager = StudentManager()

    # Adding students
    manager.add_student("Alice", "S001")
    manager.add_student("Bob", "S002")

    # Adding marks
    student = manager.find_student("S001")
    if student:
        student.input_marks("Math", 85)
        student.input_marks("English", 90)

    student = manager.find_student("S002")
    if student:
        student.input_marks("Math", 78)
        student.input_marks("English", 88)

    # List students
    manager.list_students()
