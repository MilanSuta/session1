#Author name: Milan Sutariya
#Date: 20/10/2024
#Session 5 and 6

#1
course_enrollments = {
    "Stu01": ["ICT104", "ICT107", "ICT105"],
    "Stu02": ["ICT107", "BUS105", "ICT106"],
    "Stu03": ["ICT007", "BUS109", "ICT302"],
    "Stu04": ["ICT005", "BUS105", "ICT502"],
}

for student_id, courses in course_enrollments.items():
    print(f"Student ID: {student_id}")
    print("Enrolled courses:", ", ".join(courses))
    print() 

#2
departments = {
    "ICT": [
        ("ICT104", "Introduction to Computing"),
        ("ICT107", "Data Structures"),
        ("ICT105", "Database Management"),
        ("ICT106", "Networking"),
        ("ICT302", "Advanced Computing"),
        ("ICT502", "Cybersecurity"),
    ],
    "BUS": [
        ("BUS105", "Principles of Business"),
        ("BUS109", "Business Analytics"),
    ]
}

for department, courses in departments.items():
    print("Department: ", department)
    for course in courses:
        course_id, course_name = course
        print(f"Course ID: {course_id}, Course Name: {course_name}")
    print()


#3
lecturer_Assignments = {
    "Dr. Alice Smith": ["ICT104", "ICT107"],
    "Prof. John Doe": ["BUS105", "ICT106"],
    "Dr. Emily Davis": ["ICT105", "ICT302"],
    "Prof. Michael Brown": ["BUS109", "ICT502"]
}

for lecturer, courses in lecturer_Assignments.items():
    print("Lecturer: ", lecturer)
    print("Courses taught:", ", ".join(courses))
    print()