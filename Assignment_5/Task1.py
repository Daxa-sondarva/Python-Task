
#ASSIGNMENT 5:
#Module 6: Data Structures and Strings in Python
#Task 1: Create a Dictionary of Student Marks

'''
# Step 1: Create a dictionary with student names as keys and marks as values
students_marks = {
    "daxa": 85,
    "kinjal": 92,
    "maruti": 78,
    "twinkal": 88,
    "daksha": 91
}
# Step 2: Ask the user for a student's name
student_name = input("Enter the student's name: ")

# Step 3: Retrieve and display the corresponding marks, or show a message if not found
if student_name in students_marks:
    print(f"{student_name}'s Marks: {students_marks[student_name]}")
else:
    print("Student not found!")
'''

# Step 1: Initialize an empty dictionary
students_marks = {}

# Step 2: Ask the user how many entries they want to add
num_entries = int(input("How many students' marks would you like to enter? "))

# Step 3: Loop through and get student names and marks from the user
for _ in range(num_entries):
    student_name = input("Enter the student's name: ")  # Get the student's name
    student_marks = float(input(f"Enter {student_name}'s marks: "))  # Get the student's marks

    # Step 4: Store the name and marks in the dictionary
    students_marks[student_name] = student_marks

# Display the final dictionary
print("\nFinal dictionary of students and marks:")
print(students_marks)

# Ask the user for a student's name
student_name = input("Enter the student's name: ")

# Retrieve and display the corresponding marks, or show a message if not found
if student_name in students_marks:
    print(f"{student_name}'s Marks: {students_marks[student_name]}")
else:
    print("Student not found!")
