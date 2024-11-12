# Let's write a program which assesses student's performance on a course
# The program contains 3 parts: 
# 1. reading the file, 2. processing the contents into an accessible format and 3. writing the file.

# 1st part stores the data in a dictionary, where the key is the student's name
# and the value is a list of the points received by the student, in integer format:
def read_weekly_points(filename: str) -> dict:
    weekly_points = {}

    with open(filename) as my_file:
        for line in my_file:
            parts = line.split(";")
            point_list = []
            for points in parts[1:]:
                point_list.append(int(points))
            weekly_points[parts[0]] = point_list
    
    return weekly_points

# The second function is for determining the grade based on the points received. 
def grade(points):
    if points < 20:
        return 0
    elif points < 25:
        return 1
    elif points < 30:
        return 2
    elif points < 35:
        return 3
    elif points < 40:
        return 4
    else:
        return 5

# This function is in turn used by the third function, which writes the results to the file.
def save_results(filename: str, weekly_points: dict):
    with open(filename, "w") as my_file:
        for name, point_list in weekly_points.items():
            point_sum = sum(point_list)
            my_file.write(f"{name};{point_sum};{grade(point_sum)}\n")

    return None

# Fourth added function to print out the grade
def get_grade(student_name, weekly_points):
    for name, point_list in weekly_points.items():
        if name == student_name:
            return grade(sum(point_list))
      
      
if __name__ == "__main__":
    # This structure lets us write a very simple main function.
    weekly_points = read_weekly_points("notes2.csv")
    save_results("notes2_results.csv", weekly_points)

    # If we want to add a function that prints out the grade, we can use what we've already built:
    weekly_points = read_weekly_points("notes2.csv")
    print(get_grade("Paula", weekly_points))


# Notice how each function defined above is relatively simple, and they
# all have a single resnponsibility. This approach is wise and let us add new features later on.
