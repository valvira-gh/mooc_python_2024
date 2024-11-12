# comopleted
entries = "diary_entries.txt"

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    user_function = int(input("Function: "))
    
    if user_function == 0:
        print("Bye now!")
        break
    elif user_function == 1:
        entry = input("Diary entry: ")
        with open(entries, "a") as my_file:
            my_file.write(entry + "\n")
            print("Diary saved")
    elif user_function == 2:
        print("Entries:")
        with open(entries) as my_file:
            for line in my_file:
                line = line.strip()
                print(line)
    else:
        pass



