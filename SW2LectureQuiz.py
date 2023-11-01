class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrollments = []


class Course:
    def __init__(self, course_code, course_name, instructors):
        self.course_code = course_code
        self.course_name = course_name
        self.instructors = instructors
        self.enrollments = []


class Enrollment:
    def __init__(self, student, course, progress=0.0):
        self.student = student
        self.course = course
        self.progress = progress


def enroll(student, course):
    enrollment = Enrollment(student, course)
    student.enrollments.append(enrollment)
    course.enrollments.append(enrollment)


def update_progress(student, course, progress):
    for enrollment in student.enrollments:
         if enrollment.course == course:
             enrollment.progress = progress


def print_student_enrollments(student):
    print(f"Student ID: {student.student_id}")
    print(f"Student Name: {student.name}")
    print("Enrollments:")
    for enrollment in student.enrollments:
       print(f"Course: {enrollment.course.course_name}")
       print(f"Course Code: {enrollment.course.course_code}")
       print(f"Progress: {enrollment.progress}%")
       print("Instructors:", ", ".join(enrollment.course.instructors))
       print("")


# Create students
student1 = Student(1, "Timo")
student2 = Student(2, "Phong")

# Create courses
course1 = Course("CS101", "Introduction to Python", ["Chau"])
course2 = Course("CS202", "Physics", ["Timo"])
course3 = Course("CS303", "Smart IoT", ["Kimmo"])

# Enroll students in courses
enroll(student1, course1)
enroll(student1, course2)
enroll(student2, course1)
enroll(student2, course3)

# Update progress
update_progress(student1, course1, 70.5)
update_progress(student1, course2, 85.0)
update_progress(student2, course1, 60.0)
update_progress(student2, course3, 75.5)

# Print student enrollments
print_student_enrollments(student1)
print_student_enrollments(student2)
