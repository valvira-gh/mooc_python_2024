# Deleting the file entirely we'll have to ask help from operating system
import os

# Creating a file to be deleted
with open("deletable.csv", "w") as my_file:
    my_file.write("This line is useless, because I'm going to get off'd soon.")
    my_file.close()

# A file to be printed as for exercise's sake
with open("deletable.csv") as new_file:
    for line in new_file:
        print(line)
    new_file.close()



# It is sometimes necessary to clear the contents of an existing file
# Empty write mode will do just that:
with open("deletable.csv", "w"):
    pass

# It is also possible to delete the file entirely. We'll ask OS system a little help for that.
os.remove("deletable.csv")