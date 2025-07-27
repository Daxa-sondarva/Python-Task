Assignment: 4
#Module 5 : Files, Exceptions, and Errors in Python

#Task 1: Read a File and Handle Errors
'''

file1=open('sample.txt','r')
print(file1.read())
file1.close()

'''
# Open the file in read mode
with open('sample.txt', 'r') as file:
    # Read and print each line one by one
    for line in file:
        print(line,end='')  # end='' avoids adding extra new lines
        # break