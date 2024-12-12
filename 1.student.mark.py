class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  # Dictionary to store marks by course id


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name


class School:
    def __init__(self):
        self.students = []  # List of Student objects
        self.courses = []   # List of Course objects

    def input_number_of_students(self):
        return int(input("Enter the number of students in the class: "))

    def input_student_information(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (DD/MM/YYYY): ")
        student = Student(student_id, name, dob)
        self.students.append(student)

    def input_number_of_courses(self):
        return int(input("Enter the number of courses: "))

    def input_course_information(self):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = Course(course_id, name)
        self.courses.append(course)

    def select_course_and_input_marks(self):
        course_id = input("Enter the course ID to input marks: ")
        course = next((course for course in self.courses if course.course_id == course_id), None)
        if not course:
            print("Course not found!")
            return

        for student in self.students:
            mark = float(input(f"Enter mark for {student.name} (ID: {student.student_id}): "))
            student.marks[course_id] = mark

    def list_courses(self):
        print("\nCourses:")
        for course in self.courses:
            print(f"- {course.name} (ID: {course.course_id})")

    def list_students(self):
        print("\nStudents:")
        for student in self.students:
            print(f"- {student.name} (ID: {student.student_id}, DoB: {student.dob})")

    def show_student_marks_for_course(self):
        course_id = input("Enter the course ID to view marks: ")
        course = next((course for course in self.courses if course.course_id == course_id), None)
        if not course:
            print("Course not found!")
            return

        print(f"\nMarks for course: {course.name} (ID: {course.course_id})")
        for student in self.students:
            mark = student.marks.get(course_id, "N/A")
            print(f"- {student.name} (ID: {student.student_id}): {mark}")


# Main program
school = School()

# Input students
num_students = school.input_number_of_students()
for _ in range(num_students):
    school.input_student_information()

# Input courses
num_courses = school.input_number_of_courses()
for _ in range(num_courses):
    school.input_course_information()

# Menu for managing the school system
while True:
    print("\nMenu:")
    print("1. List courses")
    print("2. List students")
    print("3. Input marks for a course")
    print("4. Show student marks for a course")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        school.list_courses()
    elif choice == "2":
        school.list_students()
    elif choice == "3":
        school.select_course_and_input_marks()
    elif choice == "4":
        school.show_student_marks_for_course()
    elif choice == "5":
        break
    else:
        print("Invalid choice! Please try again.")
