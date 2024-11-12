students = []
students_dictionary = {}
exercises = {}
exams = {}
students_points = {}


if __name__ == "__main__":
    # this is never executed
    if False:
        student_info = input("Student information: ")
        grades_data = input("Exercises completed: ")
        exam_points = input("Exam points: ")

 
    else:
        student_info = "students.csv"
        exercise_data = "exercises1.csv"
        exam_points = "exams.csv"

    with open(student_info) as new_file:
        for line in new_file:
            parts = line.split(';')
            # print('Parts:', parts[0])

            if parts[0] == "id":
                continue
            student_full_names = parts[1].strip().capitalize() + " " + parts[2].strip().capitalize()
            # students.append(student_full_names)
            students_dictionary[parts[0]] = student_full_names

        # print('Students list:', students)
        # print('Students dictionary:', students_dictionary)
    
    with open(exercise_data) as new_file:
        for line in new_file:
            parts = line.split(';')
            # print()
            # print('Exercise parts:', parts)

            if parts[0] == "id":
                continue
            # print('Parts 0:', parts[0])
            # print('Parts 1:', parts[1])

            grades = parts[1:]
            # print('Grades:', grades)

            
            last_grade = grades.pop()
            last_grade = last_grade.strip()
            grades.append(last_grade)
            # print('last grade:', last_grade)
            # print('grades:', grades)
            
            exercises[parts[0]] = grades
    
    with open(exam_points) as new_file:
        for line in new_file:
            parts = line.split(';')
            
            if parts[0] == "id":
                continue

            points = parts[1:]

            last_point = points.pop()
            last_point = last_point.strip()
            points.append(last_point)

            exams[parts[0]] = points
    

    for id, name in students_dictionary.items():
        total_points = 0
        for id in exams:
            exams_points = exams[id]
            for point in exams_points:
                point = int(point)
                total_points += point
            students_points[id] = name, total_points
    
    # print(students_points)

#     exam points + exercise points	grade
# 0-14	0 (fail)
# 15-17	1
# 18-20	2
# 21-23	3
# 24-27	4
# 28-	

    for id, stats in students_points.items():
        print(f"id: {id} || points: {stats[1]}")

        if stats[1] >= 14:
            


        
    
    # print(students_dictionary)
                


    # for id, name in students_dictionary.items():

    #     if id in exercises:
    #         grades_id = exercises[id]
    #         grades_sum = 0

    #         for grade in grades_id:
    #             grade = int(grade)
    #             grades_sum += grade

    #         print(f"{name:4} {grades_sum}")

