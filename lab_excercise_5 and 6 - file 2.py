#Author name: Milan Sutariya
#Date: 20/10/2024
#Session 5 and 6 file 2

#1
class_list = []

while True:
    student_id = input("Enter the Student ID (or type 'exit' to stop): ")
    
    if student_id.lower() == 'exit':
        break
    
    students = {
        "1001": "Alice Smith", "1002": "Bob Johnson", "1003": "Charlie Brown", "1004": "David Lee", 
        "1005": "Emily Davis", "1006": "Frank Wilson", "1007": "Grace Taylor", "1008": "Henry Anderson",
        "1009": "Isabella Thomas", "1010": "Jack Hill"
    }
    
    if student_id in students:
        student_name = students[student_id]
        class_list.append(student_name)
        print(f"{student_name} has been added to the class.")
    else:
        print("Student ID not found.")

print("\nClass List:")
for student in class_list:
    print(student)

#2
rooms = {
    "101": {"capacity": 15, "floor": "Ground Floor", "location": "Building A"},
    "102": {"capacity": 15, "floor": "Ground Floor", "location": "Building A"},
    "103": {"capacity": 20, "floor": "Ground Floor", "location": "Building A"},
    "106": {"capacity": 25, "floor": "Ground Floor", "location": "Building A"},
    "206": {"capacity": 40, "floor": "1st Floor", "location": "Building A"}
}

min_seats = int(input("Enter the minimum number of seats required for the class: "))

print("\nRooms that can support the required number of students:")
for room_number, details in rooms.items():
    if details['capacity'] >= min_seats:
        print(f"Room {room_number}: Capacity {details['capacity']}, Floor {details['floor']}, Location {details['location']}")

if not any(details['capacity'] >= min_seats for details in rooms.values()):
    print("No rooms available with the required capacity.")


#3.1
class_list = []

while True:
    student_id = input("Enter the Student ID (or type 'quit', 'exit', or '0' to stop): ")
    
    if student_id.lower() in ['quit', 'exit', '0']:
        exit_param = student_id.lower()
        break
    
    students = {"1001": "Alice Smith", "1002": "Bob Johnson", "1003": "Charlie Brown", "1004": "David Lee"}
    
    if student_id in students:
        student_name = students[student_id]
        class_list.append(student_name)
        print(f"{student_name} has been added to the class.")
    else:
        print("Student ID not found.")

print(f"\nClass List: {class_list}")
print(f"Total number of students: {len(class_list)}")
print(f"Exited using: {exit_param}")

#3.2
class_list = []
active = True

while active:
    student_id = input("Enter the Student ID (or type 'stop' to end): ")
    
    if student_id.lower() == 'stop':
        active = False
    else:
        students = {"1001": "Alice Smith", "1002": "Bob Johnson", "1003": "Charlie Brown", "1004": "David Lee"}
        if student_id in students:
            student_name = students[student_id]
            class_list.append(student_name)
            print(f"{student_name} has been added to the class.")
        else:
            print("Student ID not found.")

print(f"\nClass List: {class_list}")
print(f"Total number of students: {len(class_list)}")

#3.3
class_list = []
max_cap = 5

while True:
    student_id = input(f"Enter the Student ID (Room capacity: {max_cap}, Students added: {len(class_list)}): ")
    
    if len(class_list) < max_cap:
        students = {"1001": "Alice Smith", "1002": "Bob Johnson", "1003": "Charlie Brown", "1004": "David Lee"}
        if student_id in students:
            student_name = students[student_id]
            class_list.append(student_name)
            print(f"{student_name} has been added to the class.")
        else:
            print("Student ID not found.")
    else:
        print("\nRoom capacity reached.")
        break

print(f"\nClass List: {class_list}")
print(f"Total number of students: {len(class_list)}")
print(f"Maximum capacity: {max_cap}")

#4
line_count = 0

try:
    while True:
        user_input = input("Enter some text (Press CTRL-C to exit): ")
        
        print(user_input)
        
        line_count += 1
except KeyboardInterrupt:
    print("\nProgram interrupted by CTRL-C.")
    print(f"Total number of lines entered: {line_count}")
