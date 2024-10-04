units_list = [
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

def Retr_cour_data(course_id):
    """Retrieve course data from the units list by course ID."""
    for unit in units_list:
        if unit[0] == course_id:
            return unit
    return None

def main():
    while True:
        user_input = input("Enter a course ID to retrieve its details (1-10), or type 'quit' to exit: ")

        if user_input.lower() == "quit":
            print("Exiting the program...")
            break

        if user_input.isdigit():
            course_id = int(user_input)
            course_data = Retr_cour_data(course_id)
            if course_data:
                print(f"\nCourse ID: {course_data[0]}\n"
                      f"Course Name: {course_data[1]}\n"
                      f"Department: {course_data[2]}\n"
                      f"Prerequisites: {course_data[3]}\n")
            else:
                print(f"No course found with ID {course_id}. Please enter a valid ID.")
        else:
            print("Invalid input. Please enter a valid course ID or 'quit'.")

if __name__ == "__main__":
    main()