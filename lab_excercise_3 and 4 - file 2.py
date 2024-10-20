units = [
    [1, "Introduction to Programming", "Computer Science", "None"],
    [2, "Calculus I", "Mathematics", "None"],
    [3, "Data Structures and Algorithms", "Computer Science", "Introduction to Programming"],
    [4, "Linear Algebra", "Mathematics", "Calculus I"],
    [5, "Physics I", "Physics", "None"],
    [6, "Chemistry I", "Chemistry", "None"],
    [7, "Biology I", "Biology", "None"],
    [8, "Microeconomics", "Economics", "None"],
    [9, "Macroeconomics", "Economics", "None"],
    [10, "Psychology I", "Psychology", "None"],
]

def get_course_info(course_id):
    for unit in units:
        if unit[0] == course_id:
            return unit
    return None  
def run_program():
    while True:
        user_input = input("Enter a course ID between 1 to 10, or type 'quit' to exit: ")
        
        if user_input == "quit":  
            print("Exiting now...")
            break  
        
        if user_input.isdigit():  
            course_id = int(user_input)  
            course_info = get_course_info(course_id)
            
            if course_info:  
                print("\nCourse ID: ", course_info[0])
                print("Course Name: ", course_info[1])
                print("Department: ", course_info[2])
                print("Prerequisites: ", course_info[3])
            else:
                print("Sorry, no course found with ID!!", course_id)
        else:
            print("Invalid input. Please enter a number between 1 to 10 or 'quit'.")

if __name__ == "__main__":
    run_program()
