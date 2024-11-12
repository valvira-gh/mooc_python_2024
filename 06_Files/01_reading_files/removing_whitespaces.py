# Excel is notorious for adding extra whitespace
# We would like to print out the last names of each person on the list
# The first line contains headers for the data, and it can be safely ignored
last_names = []
with open("people.csv") as new_file:
    for line in new_file:
        parts = line.split(";")
        # ignore the header line
        if parts[0] == "first":
            continue
        last_names.append(parts[1].strip()) # added strip()
print(last_names)

# strip()-string method removes extra spaces, line breaks and other chars, which would be normally printed
