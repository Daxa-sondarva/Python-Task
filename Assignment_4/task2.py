Assignment: 4
#Module 5 : Files, Exceptions, and Errors in Python

## Task 2: Write and Append Data to sample.txt

# Step 1: Write user input to the file
user_input = input("Enter some data to write to the file: ")

# Open the file in write mode and write the user input to it
with open('sample.txt', 'a') as file:  # Open in 'a' mode to append to existing file
    file.write(user_input + '\n')  # Add a newline after the input

# Step 2: Append additional data to the file
additional_data = "Additional data appended to sample.txt."
with open('sample.txt', 'a') as file:
    file.write(additional_data + '\n')  # Append the additional data

# Step 3: Read and display the final content of the file
print("\nFinal content of sample.txt:")
with open('sample.txt', 'r') as file:
    print(file.read())  # Print the entire content of the file


