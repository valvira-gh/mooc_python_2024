# Let's use personal identity code (PIC) for identifying the data from two of the files

# At first we create names dictionary to store the names of the employees
names = {}

with open("employees.csv") as new_file:
    for line in new_file:
        parts = line.split(";")
        # Use pic for identifying
        if parts[0] == "pic":
            continue
        # Use pic as a key and data as a value
        names[parts[0]] = parts[1]

salaries = {}

with open("salaries.csv") as new_file:
    for line in new_file:
        parts = line.split(";")
        # Same here
        if parts[0] == "pic":
            continue
        # Modify data types from strings to ints
        salaries[parts[0]] = int(parts[1]) + int(parts[2])

print("incomes:")

# Loop over both dictionaries and use pic as for identifying
for pic, name in names.items():
    # Check if the person is included in data
    if pic in salaries:
        # If they are, store salary in to variable and print it out
        salary = salaries[pic]
        # ':16' refers to spacing in which the data is printed out
        print(f"{name:16} {salary} euros")
    else:
        print(f"{name:16} 0 euros")

# incomes:
# Pekka Mikkola    3300 euros
# Liisa Marttinen  4350 euros
# Arto Vihavainen  2500 euros
# Leevi Hellas     0 euros