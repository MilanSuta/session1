#Author name: Milan Sutariya
#Date: 20/10/2024
#Session 5 and 6

#1
course_enrollments = {
    "1001": ["CS101", "MATH101", "PHY101"],
    "1002": ["CS202", "MATH102", "CHEM101"],
    "1003": ["BIO101", "ENGL101", "HIST101"],
    "1004": ["SOC101", "PSY101", "ECON101"]
}

for student_id, courses in course_enrollments.items():
    print(f"Student ID: {student_id}")
    print("Enrolled courses:", ", ".join(courses))
    print()

#2
departments = {
    "Computer Science": [
        ("CS101", "Introduction to Computer Science"),
        ("CS202", "Data Structures and Algorithms")
    ],
    "Mathematics": [
        ("MATH101", "Calculus I"),
        ("MATH102", "Calculus II")
    ],
    "Physics": [
        ("PHY101", "General Physics I"),
        ("PHY102", "General Physics II")
    ],
    "Chemistry": [
        ("CHEM101", "General Chemistry I"),
        ("CHEM102", "General Chemistry II")
    ],
    "Biology": [
        ("BIO101", "Biology I"),
        ("BIO102", "Biology II")
    ]
}

for department, courses in departments.items():
    print("Department: ", department)
    for course in courses:
        course_id, course_name = course
        print(f"Course ID: {course_id}, Course Name: {course_name}")
    print()

#3
lecturer_assignments = {
    "Dr. Sarah Collins": ["CS101", "CS202"],
    "Prof. Mark Evans": ["MATH101", "MATH102"],
    "Dr. Robert Thompson": ["PHY101", "PHY102"],
    "Prof. Jennifer Parker": ["CHEM101", "BIO101"],
    "Dr. Emily Davis": ["BIO102", "ENGL101"],
    "Prof. Michael Scott": ["SOC101", "PSY101"],
    "Dr. James Smith": ["ECON101", "HIST101"]
}

for lecturer, courses in lecturer_assignments.items():
    print("Lecturer: ", lecturer)
    print("Courses taught:", ", ".join(courses))
    print()
