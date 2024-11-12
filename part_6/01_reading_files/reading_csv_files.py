# A CSV file, short for comma-separated values, is a text file which contains data separated by
# a predetermined character. The most common char's for this purpose are `,` and `;`.

# CSV files are commonly used to store records of different kinds. Many DB's and spreadsheet
# programs, such as Excel, can import and export data in CSV format, which makes data exchange between
# different systems easy.

# We already know how to read files line by line, but how we can separate the different fields on a single line?
# Python has a string-method called 'split()' for this purpose. The method takes the separator character(s) as a 
# string argument and returns the contents of the target string as a _list of strings_, separated at the separator.

# EXAMPLE 1:
# text = "monkey,banana,harpsichord,uuvat"
# words = text.split(",")
# for word in words:
#     print(word)

# monkey
# banana
# harpsichord
# uuvat

# EXAMPLE 2:
with open("grades.csv") as new_file:
    for line in new_file:
        line = line.rstrip()
        parts = line.split(";")
        name = parts[0]
        grades = parts[1:]
        print("Name:", name)
        print("Grades:", grades)
        print()

