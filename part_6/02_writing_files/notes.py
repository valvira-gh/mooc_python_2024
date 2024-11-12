# Use 'w' (write) as second argument of the open()-function, when writing files
with open("new_file.txt", "w") as my_file:
    # code to write something to the file
    my_file.write("Hello there!")

    # added texts doesn't include '\n' at the end of the line, so if you want line breaks, add '\n'
    my_file.write("this goes right next to '!', but the next line goes to the next line\n")
    my_file.write("Yey! A line break!\n")


# APPENDING DATA
# If you want to append data to the end of a file, instead of overwriting the entire file
# you should open the file append mode with the second argmument as 'a' (append)
with open("new_file.txt", "a") as my_file:
    my_file.write("This line is appended.\n")
# appending data is not very common practice in programming


# WRITING CSV-FILES
# CSV files can be written as any other file by write-method and using semicolons
# with open("coders.csv", "w") as my_file:
#     my_file.write("Eric;Windows;Pascal;10\n")
#     my_file.write("Matt;Linux;PHP;2\n")
#     my_file.write("Alan;Linux;Java;17\n")
#     my_file.write("Emily;Mac;Cobol;9\n")

# What if the data to be written is stored in copmuter memory in a list?
coders = []
coders.append(["Eric", "Windows", "Pascal", 10])
coders.append(["Matt", "Linux", "PHP", 2])
coders.append(["Alan", "Linux", "Java", 17])
coders.append(["Emily", "Mac", "Cobol", 9])

# We can use the f-string to accomplish what we want
with open("coders.txt", "w") as my_file:
    for coder in coders:
        line = f"{coder[0]};{coder[1]};{coder[2]};{coder[3]}"
        my_file.write(line+"\n")

# But more easier is to use for loop for accessing long data lists
with open("coders.csv", "w") as my_file:
    for coder in coders:
        line = ""
        for value in coder:
            line += f"{value};"
        line = line[:-1]
        my_file.write(line + "\n")




