#Author name: Milan Sutariya
#Date and Time: 24/09/2024 ___ 01:37pm
#Task: session 3 and 4 SUBMISSION file
 
#1.1
course_list = ["Introduction to Programming", "Calculus I", "Data Structures and Algorithms", "Linear Algebra", "Physics I", "Chemistry I", "Discrete Mathematics", 
                "Biology I", "Microeconomics", "Macroeconomics", "Psychology I ", "History I", "English Composition I", "Introduction to Philosophy", "Calculus II"]

#1.2
print("")
print("Course list is",course_list)

#2.1
print("")
course_list = sorted(course_list)

#2.2
print("")
print("Sorted Course list is",course_list)

#2.3
course_list = sorted(course_list, reverse=True)

#2.4
print("")
print("Sorted reverse Course list is",course_list)

#3.1
course_list.reverse()

#3.2
print("")
print("after using reverse on list", course_list)

#3.3
course_list.reverse()

#3.4
print("")
print("after using reverse on list", course_list)

#4.1
course_list.sort()

#4.2
print("")
print("after sort function on last saved course list", course_list)

#4.3
course_list.sort(reverse=True)

#4.4
print("")
print("after using sort function with perameter reverse", course_list)

##############        task done till page number 2        ##############
print("\n----------------Task done till page 2----------------")

course_list = ["Introduction to Programming", "Calculus I", "Data Structures and Algorithms", "Linear Algebra", "Physics I", "Chemistry I", "Discrete Mathematics"]

#1.1 and 1.2
course_list.sort()
print("\nThe following courses are available for expression of interest if the students meet the prerequisites:\n")
for course in course_list:
    print(course)

#2.1 and 2.2
print("\nOne of the course is not availabe in given list. The course name is CALCULUS I and that course is replaceable with  PHYSICS I")
withdrawn_course = "Calculus I"
new_course = "Physics I"
print("\nHere is the orginal course list:")
for course in course_list:
    print(course)
print("\nHere is the new list of available course:")
course_list[course_list.index(withdrawn_course)] = new_course
for course in course_list:
    print(course)

#3.1, 3.2, 3.3, 3.4 and 3.5
course_list = ["Physics I", "Chemistry I", "Data Structures and Algorithms", 
               "Discrete Mathematics", "English Composition I", "Introduction to Philosophy", 
               "Introduction to Programming", "Linear Algebra"]
newCourse= ["Biology I", "Macroeconomics", "Psychology I"]
course_list.insert(0, newCourse[0])
course_list.insert(len(course_list) // 2, newCourse[1])
course_list.append(newCourse[2])
print("\nThe updated course list with new courses added is:")
for course in course_list:
    print(course)


#4.1, 4.2, 4.3 and 4.4
course_list = ["Biology I", "Physics I", "Chemistry I", "Data Structures and Algorithms", "Discrete Mathematics", "English Composition I", "Introduction to Philosophy", 
               "Introduction to Programming", "Linear Algebra", "Macroeconomics", "Psychology I"]
unavailable_courses = []
print("\nDue to technical and room availability issues, the following courses are no longer available:")
for i in range(4):
    removed_course = course_list.pop()
    unavailable_courses.append(removed_course)
    print(removed_course)
print("\nThe updated list of available courses is:")
for course in course_list:
    print(course)

##############        task done till page number 3        ##############
print("\n----------------Task done till page 3----------------")

#1.1 and 1.2
courses = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics I"),
    (6, "Chemistry I"),
    (7, "Biology I"),
    (8, "Microeconomics"),
    (9, "Macroeconomics"),
    (10, "Psychology I"),
    (11, "History I"),
    (12, "English Composition I"),
    (13, "Introduction to Philosophy"),
    (14, "Calculus II"),
    (15, "Discrete Mathematics")
]
course_ids_and_names = []

#2.1 and 2.2
for course in courses:
    course_id, course_name = course
    course_ids_and_names.append(course_name)

print("\n",course_ids_and_names)

#3
print("\nCourse Information:")
for course in courses:
    course_id = course[0]
    course_name = course[1]
    print("Course ID and Course Name:", course_id,",", course_name)

#################
#
#
#
#
#
########################      SESSION 4      ########################
#
#
#
#
#
#################


# 1. Conditional statement
courses = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics I"),
    (6, "Chemistry I"),
    (7, "Biology I"),
    (8, "Microeconomics"),
    (9, "Macroeconomics"),
    (10, "Psychology I"),
    (11, "History I"),
    (12, "English Composition I"),
    (13, "Introduction to Philosophy"),
    (14, "Calculus II"),
    (15, "Discrete Mathematics")
]

user_input = int(input("\nEnter the course ID you want to search for: "))
course_found = False

for course in courses:
    if course[0] == user_input:
        print(f"\nThe course name for ID {user_input} is: {course[1]}")
        course_found = True
        break
if not course_found:
    print(f"\nNo course found with ID {user_input}.")


while True:
    user_input = input("Enter a command (type 'quit' or '0' to exit): ")
    
    if user_input.lower() == "quit" or user_input == "0":
        print("Exiting the loop...")
        break
    else:
        print("user input is", user_input)

while True:
    user_input = input("Enter a course ID, or type 'quit' or '0' to exit: ")

    if user_input.lower() == "quit" or user_input == "0":
        print("Exiting the program...")
        break

    if user_input.isdigit():
        course_id = int(user_input)
        course_found = False
        
        for course in courses:
            if course[0] == course_id:
                print(f"Course ID {course_id} corresponds to: {course[1]}")
                course_found = True
                break
        
        if not course_found:
            print(f"No course found with ID {course_id}.")
    else:
        print("Invalid input. Please enter a valid course ID, 'quit', or '0'.")

# Sample course data
courses = [
    (1, "Introduction to Programming", "Computer Science"),
    (2, "Calculus I", "Mathematics"),
    (3, "Data Structures and Algorithms", "Computer Science"),
    (4, "Linear Algebra", "Mathematics"),
    (5, "Physics I", "Physics"),
    (6, "Chemistry I", "Chemistry"),
    (7, "Biology I", "Biology"),
    (8, "Microeconomics", "Economics"),
    (9, "Macroeconomics", "Economics"),
    (10, "Psychology I", "Psychology"),
]

while True:
    user_input = input("Enter a course ID, or type 'quit' or '0' to exit: ")

    if user_input.lower() == "quit" or user_input == "0":
        print("Exiting the program...")
        break

    if user_input.isdigit():
        course_id = int(user_input)
        course_found = False
        
        for course in courses:
            if course[0] == course_id:
                print(f"The course department for ID {course_id} is: {course[2]}")
                course_found = True
                break
        
        if not course_found:
            print(f"No course found with ID {course_id}.")
    else:
        print("Invalid input. Please enter a valid course ID, 'quit', or '0'.")

while True:
    user_input = input("Enter a course ID (1-15)")

    if user_input.isdigit():
        course_id = int(user_input)

        if 1 <= course_id <= 15:
            for course in courses:
                if course[0] == course_id:
                    print(f"Course ID {course_id} is in the {course[2]} department.")
                    break
            break
        else:
            print("Course ID is out of range (1-15), try again.")

