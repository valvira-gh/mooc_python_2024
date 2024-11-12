with open("numbers.txt") as new_file:
    largest_num = 0
    count = 1
    lines = []

    for line in new_file:
        line = line.replace("\n", "")
        
        line = int(line)

        if line > largest_num:
            largest_num = line
        
        count += 1

    print('Largest num:', largest_num)
