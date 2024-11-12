# new_file is a file handle
# with open("example.txt") as new_file:
#     contents = new_file.read()
#     print(contents)

# Text files can be thought of as lists of strings, each string representing a single line in the file. 
# We can go through the list with a for loop.

with open("example.txt") as new_file:
    count = 0
    total_length = 0

    for line in new_file:
        # removes the line break
        line = line.replace("\n", "")
        count += 1
        print("Line", count, line)
        length = len(line)
        total_length += length

print("Total length of lines:", total_length)

# PRINTS:
# Line 1 Hello there!
# Line 2 This example file contains three lines of text.
# Line 3 This is the last line.
# Total length of lines: 81

