Assignment: 4
#Module 5 : Files, Exceptions, and Errors in Python

#Task 1: Read a File and Handle Errors

'''
file1=open('sample.txt','r')
print(file1.read())
file1.close()
'''
# Exception handaling using try Except block
try:
    # Open the file in read mode
    with open('sample.txt', 'r') as file:
        # Read and print the file line by line
        print("Content of sample.txt:")
        for line in file:
            print(line, end='')  # Print each line without adding extra newlines
except FileNotFoundError:
    # Handle the case where the file does not exist
    print("Error: The file 'sample.txt' does not exist.")

